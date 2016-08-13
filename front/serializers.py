from django.forms import widgets
from rest_framework import serializers
from front.models import Urls

class UrlsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Urls
        fields = ('id', 'short', 'long', 'status', 'title', 'wayback', 'timestamp')
