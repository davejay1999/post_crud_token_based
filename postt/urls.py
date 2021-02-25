
from django.contrib import admin
from django.urls import path,include
from rest_framework.authtoken import views 
from django.views.generic.base import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('posts/',include('posts.urls')),
    path('api-token-auth/', views.obtain_auth_token, name='api-tokn-auth'),
    path('', RedirectView.as_view(url='posts/', permanent=False), name='index')
  #  path('api-auth/', include('rest_framework.urls')),
]
