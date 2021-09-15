from django.shortcuts import render
from rest_framework.views import APIView, Response

# Create your views here.


class TestView(APIView):
    def get(self, request, *args, **kwargs):
        data = {
            "msg": "Hello, World!"
        }
        return Response(data)
