# main > views.py

from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny


class IndexView(APIView):
    permission_classes = [AllowAny]

index = IndexView.as_view()