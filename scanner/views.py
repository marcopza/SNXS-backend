from django.shortcuts import render
from rest_framework.views import APIView, Response
from rest_framework import status
import validators
from . import scanner


class ScannerView(APIView):

    def post(self, request, *args, **kwargs):

        if "url" not in request.data or "cookie" not in request.data or "type" not in request.data:
            return Response({
                "error": "Please provide all necessary parameters"
            }, status=status.HTTP_400_BAD_REQUEST)
        url = request.data["url"]
        cookie = request.data["cookie"]
        test_type = request.data["type"]
        if test_type == "":
            return Response({
                "error": "No test was selected"
            }, status=status.HTTP_400_BAD_REQUEST)
        response = {}
        if validators.url(url):
            if "1" in test_type:
                response["SQLi"] = scanner.check_sqli(url, cookie)
            if "2" in test_type:
                response["NoSQLi"] = scanner.check_nosqli(url)
            if "3" in test_type:
                response["XSS"] = scanner.check_xss(url, cookie)
            if not response:
                return Response({
                    "error": "Please provide valid test options"
                }, status=status.HTTP_400_BAD_REQUEST)
            return Response({"data": response}, status=status.HTTP_200_OK)
        return Response({
            "error": "Please provide a valid url"
        }, status=status.HTTP_400_BAD_REQUEST)
