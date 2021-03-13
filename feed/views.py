import requests
from bs4 import BeautifulSoup
from django.shortcuts import render

# Create your views here.
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from feed.models import FeedModel
from feed.serializers import FeedSerializer

urls = [
    {"id": 1, "link": "https://www.buzzfeed.com/world.xml"},
    {"id": 2, "link": "http://feeds.bbci.co.uk/news/video_and_audio/news_front_page/rss.xml?edition=uk"},
    {"id": 3, "link": "https://www.nytimes.com/svc/collections/v1/publish/https://www.nytimes.com/section/world/rss.xml"},
    ]


class FeedView(APIView):

    @classmethod
    def get(cls, request):
        RssDataArray = []
        if len(FeedModel.objects.all()) == 0:
            for url in urls:
                feed_candidate = FeedModel(link=url['link'])
                feed_candidate.save()
        feed_list = FeedModel.objects.all()
        for feed in feed_list:
            response = requests.get(FeedSerializer(feed).data['link'])
            soup = BeautifulSoup(response.content, features='xml')
            RssDataArray.append({'id': FeedSerializer(feed).data['id'], 'data': soup.prettify(), 'link': FeedSerializer(feed).data['link']})
        return Response(RssDataArray, status=200)


class DeleteFeedView(APIView):

    @classmethod
    def delete(cls, request: Request, id):
        delete_candidate = FeedModel.objects.filter(id=id)
        delete_candidate.delete()
        return Response(FeedSerializer(FeedModel.objects.all(), many=True).data, status=200)


class CreateFeedView(APIView):

    @classmethod
    def post(cls, request: Request):
        print(request.data)
        candidate = FeedModel(link=request.data['link'])
        candidate.save()
        return Response({'OK'}, status=200)
