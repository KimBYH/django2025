from django.http import HttpResponse
from django.shortcuts import render

from product.models import MainContent


def index(req) :
    return render(req,'pages/company.html')

def company(req) :
    return render(req, 'pages/company_info.html')

def library(req) :
    return render(req, 'pages/mainpage.html')

#Create your views here.
