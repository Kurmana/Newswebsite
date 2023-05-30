from django.urls import path
from .views import *

urlpatterns = [
    path('', home),
    path('contact', contact),
    path('news/<int:id>', news_detail),
    path('category/<int:id>', category_news),
]
