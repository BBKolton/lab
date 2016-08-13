from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from front.models import Urls
from front.serializers import UrlsSerializer
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as loginFunc, logout as logoutFunc
import requests
import re #regex

def index(request): 
    urls = Urls.objects.all()
    if (request.user.is_authenticated()):
        return render(request, 'home.html', {'urls': urls})
    else:
        return render(request, 'unauthed.html', {'urls': urls})


def logout(request):
    logoutFunc(request)
    return redirect('/lab/');


def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')

    else:
        user = authenticate(username=request.POST['username'], password=request.POST['password'])
        if user is not None:
            loginFunc(request, user)   
            return redirect('/lab/')
        else:
            return render(request, 'login.html', {'mess': "Invalide username or password"})
    

@api_view(['GET', 'POST'])
def listall(request, format=None):
    print('herp derp')
    if request.method == 'GET':
        urls = Urls.objects.all()
        serializer = UrlsSerializer(urls, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':

        if request.user.is_authenticated() is False:
            return Response(status=HTTP_400_BAD_REQUEST)


        r = requests.get(request.POST['short'])

        title = re.search(r'<title>.+</title>', r.text)
        title = re.sub(r'<title>|</title>', '', title.group(), count=2)


        wayback = requests.get('http://archive.org/wayback/available?url=' + r.url).json()

        print("this is the wayback response")
        print(wayback['archived_snapshots']['closest']['url'])

        archive = wayback['archived_snapshots']['closest']['url']
        timestamp = wayback['archived_snapshots']['closest']['timestamp']

        print(archive)
        print(timestamp)

        serializer = UrlsSerializer(data={'short': request.POST['short'],
                                          'long': r.url,
                                          'status': r.status_code,
                                          'wayback': archive,
                                          'timestamp': timestamp,
                                          'title': title})


        print(r.url)

        if serializer.is_valid():
            serializer.save()
            #return Response(serializer.data, status=status.HTTP_201_CREATED)
            return redirect('/lab/')
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def url(request, pk, format=None):
    """
    Retrieve, update or delete a Url.
    """
    try:
        url = Urls.objects.get(pk=pk)
    except Urls.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = UrlsSerializer(url)
        return Response(serializer.data)

    if request.user.is_authenticated() is False:
        return redirect('/log/labin/')

    if request.method == 'PUT':
        serializer = UrlsSerializer(url, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'DELETE':
        url.delete()
        return redirect('/lab/')

def deleteurl(request, pk, format=None):
    if request.user.is_authenticated() is False:
        return redirect('/lab/login/')
    
    try:
        url = Urls.objects.get(pk=pk)
    except Urls.DoesNotExist:
        return 404

    url.delete()
    return redirect('/lab')
