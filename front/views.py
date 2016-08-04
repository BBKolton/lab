from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from front.models import Urls
from front.serializers import UrlsSerializer
from django.shortcuts import render

def index(request):
    urls = Urls.objects.all()
    return render(request, 'home.html', {'urls': urls})

@api_view(['GET', 'POST'])
def listall(request, format=None):
    if request.method == 'GET':
        urls = Urls.objects.all()
        serializer = UrlsSerializer(urls, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = UrlsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
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

    elif request.method == 'PUT':
        serializer = UrlsSerializer(url, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        url.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
