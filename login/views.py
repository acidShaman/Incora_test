from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from rest_framework.views import APIView

users = [
    {'username': 'andrew', 'password': 'motruk'},
    {'username': 'john', 'password': 'doe'},
]


class LoginView(APIView):

    @classmethod
    def post(cls, request):
        print(request.data)
        candidate = [user for user in users if user['username'] == request.data['username']]
        if len(candidate) >= 1 and candidate[0]['password'] == request.data['password']:
            return Response({'Logged In'}, status=200)
        return Response({'Wrong Credentials'}, status=401)
