from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.core.permissions import IsAdmin


class A(APIView):
    permission_classes = [IsAdmin]

    def get(self, request, format=None):
        return Response("s")
