from django.contrib import admin
from django.urls import path
from .views import *
from django.views.generic.base import RedirectView

urlpatterns = [

    path('post/', PostView.as_view()),
    path('post/<str:pk>/', PostViewDetail.as_view()),
    path('', RedirectView.as_view(url='post/', permanent=False), name='index')

]