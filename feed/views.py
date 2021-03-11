import requests
from bs4 import BeautifulSoup
from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from rest_framework.views import APIView

url = "https://www.nasa.gov/rss/dyn/breaking_news.rss"


class FeedView(APIView):

    @classmethod
    def get(cls, request):
        response = requests.get(url)
        soup = BeautifulSoup(response.content, features='xml')
        return Response(soup.prettify(), status=200)

