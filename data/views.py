from django.shortcuts import render
from .models import Post
# Create your views here.

def New_Post(request) :
    Data = {
        'Posts': Post.objects.all().order_by('-date')[:5], 
        'SW': Post.objects.filter(category__endswith = 'wars'),
        'NG': Post.objects.filter(category__endswith = 'ninjago')
    }
    return render(request, 'datalist/new_post.html', Data)

def New_All(request) :
    All = {"All" : Post.objects.all().order_by('-date')}
    return render(request, 'datalist/new_all.html', All)

def Detail(request, id) :
    DT = Post.objects.get(id = id)
    return render(request, 'datalist/detail.html', {"DT" : DT})