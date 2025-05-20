from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from django.shortcuts import render

from product.models import MainContent

def index(req) :
    content_list = MainContent.objects.order_by('-pub_date')
    context = {'content_list': content_list}
    return render(req, 'product/index.html', context)

def detail(req, content_id):
    content_list = get_object_or_404(MainContent, id=content_id)
    context={'content_list' : content_list}
    return render(req,'product/content_detail.html', context)

# Create your views here.
