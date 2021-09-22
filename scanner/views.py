from django.shortcuts import render
from rest_framework.views import APIView, Response
from rest_framework import status
import validators
from . import scanner

# Create your views here.


class ScannerView(APIView):

    def post(self, request, *args, **kwargs):
        url = request.data["url"]
        cookie = request.data["cookie"]
        if validators.url(url):
            return Response(scanner.check_sqli(url, cookie), status=status.HTTP_200_OK)
        return Response("Fail", status=status.HTTP_400_BAD_REQUEST)
