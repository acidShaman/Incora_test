import requests
from bs4 import BeautifulSoup
from django.shortcuts import render

# Create your views here.
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView


class ArticleView(APIView):

    @classmethod
    def post(cls, request: Request):
        link = request.data['link'][0].strip()
        response = requests.get(link)
        soup = BeautifulSoup(response.content, features='lxml')
        return Response(soup.prettify(), status=200)

