from django.core.exceptions import PermissionDenied
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import  login_required
from .models import  MainContent, Comment
from .forms import CommentForm


def index(req) :
    content_list = MainContent.objects.order_by('-pub_date')
    context = {'content_list': content_list}
    return render(req, 'product/index.html', context)

def detail(req, content_id):
    content_list = get_object_or_404(MainContent, id=content_id)
    context={'content_list' : content_list}
    return render(req,'product/content_detail.html', context)

@login_required(login_url="accounts:login")
def comment_create(req, content_id) :
    content_list = get_object_or_404(MainContent, pk=content_id)

    if req.method == "POST" :
        form = CommentForm(req.POST)
        if form.is_valid() :
            comment = form.save(commit = False)
            comment.content_list = content_list
            comment.author = req.user
            comment.save()
            return redirect('detail', content_id = content_list.id)
    else :
        form = CommentForm()

    context = {'content_list': content_list, 'form': form}
    return render(req, 'product/content_detail.html', context)

@login_required(login_url='accounts:login')
def comment_update(request, comment_id):
    comment = get_object_or_404(Comment, pk=comment_id)
    if request.user != comment.author:
        raise PermissionDenied
    if request.method == 'POST':
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.save()
            return redirect('detail', content_id=comment.content_list.id)
    else:
        form = CommentForm(instance=comment)
    context = {'comment': comment, 'form': form}
    return render(request, 'product/comment_form.html', context)

@login_required(login_url="accounts:login")
def comment_delete(req, comment_id):
    comment = get_object_or_404(Comment, pk=comment_id)

    if req.user != comment.author:
        raise PermissionDenied
    else:
        comment.delete()
    return redirect('detail', content_id = comment.content_list.id)
# Create your views here.
