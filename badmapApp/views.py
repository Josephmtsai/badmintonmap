from django.shortcuts import render

import os
# Create your views here.
from django.http import HttpResponse
from crawler import googleExcelCrawler
def home(request):
    s = "Hello World!"
    return HttpResponse(s)



def apiCrawler(request):
    return response("OK")