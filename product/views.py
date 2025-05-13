from django.http import HttpResponse
from django.shortcuts import render

from product.models import MainContent

def index(req) :
    content_list = MainContent.objects.order_by('-pub_date')
    context = {'content_list': content_list}
    return render(req, 'product/index.html', context)


# Create your views here.
