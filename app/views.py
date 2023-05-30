from django.shortcuts import render
from .models import *
from .forms import *


def home(request):
    news = News.objects.all()
    categories = Category.objects.all()
    related_news = News.objects.all().order_by('?')[:3]
    return render(request, 'index.html', {'news': news, 'categories': categories, 'related_news': related_news})


def category_news(request, id):
    category = Category.objects.get(id=id)
    news = News.objects.filter(category=category)
    related_news = News.objects.all().order_by('?')[:3]
    categories = Category.objects.all()
    return render(request, 'index.html', {'news': news, 'categories': categories, 'category': category, 'related_news': related_news})


def news_detail(request, id):
    news = News.objects.get(id=id)
    categories = Category.objects.all()
    if request.method == 'POST':
        form = CommentForm(data=request.POST)
        data = form.save(commit=False)
        data.news = news
        data.save()

    related_news = News.objects.all().order_by('?')[:3]
    form = CommentForm()
    return render(request, 'news_detail.html', {'news': news, 'categories': categories, 'related_news': related_news, 'form': form})


def get_news(request, id):
    news = News.objects.get(id=id)
    return render(request, 'news_detail.html', {'news': news})


def contact(request):
    related_news = News.objects.all().order_by('?')[:3]
    return render(request, 'contact.html', {'related_news': related_news})




