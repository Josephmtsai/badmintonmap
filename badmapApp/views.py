from django.shortcuts import render

import os
# Create your views here.
from django.http import HttpResponse
from crawler import googleExcelCrawler
def home(request):
    s = "Hello World!"
    return HttpResponse(s)



def apiCrawler(request):
    return esponse(googleExcelCrawler.syncExcelToDB(os.environ.get('MONGODB_URI'),"1sdEYj_w57iQaFhD5eNNOMLEhMbzlnhs7vR8Lz5RlChA"))