"""
URL configuration for pact11_12 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls.py import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls.py'))
"""
from django.contrib import admin
from django.urls import path, include
from pract_11.urls import pract_11_urls
from pract_12.urls import pract_12_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path("ryzhkov/", include(pract_11_urls)),
    path("", include(pract_12_urls))
]
