from blog.models import Blogpost
from django.shortcuts import render
from django.http import HttpResponse
from . models import Blogpost
# Create your views here.
def index(request):
    blogposts=Blogpost.objects.all()
    print(blogposts)
    params={'blogposts':blogposts}
    return render(request,"blog/index.html",params)
def blogpost(request,id):
    post=Blogpost.objects.filter(post_id=id)[0]
    return render(request,"blog/blogpost.html",{'post':post})
