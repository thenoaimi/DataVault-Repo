
"""login URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf import settings
from django.urls import path, include
from django.conf.urls.static import static
from . import views
app_name = 'TEST'
urlpatterns = [
    path('', views.dataprocess),
    path('experiment1/',views.experiment1),
    path('experiment2/',views.experiment2),
    path('probedata/', views.probedata,name='probedata'),
    path('probedata/plot/', views.plot, name='plot'),
    path('fNIRsdata/plot/', views.fNIRs),
    ]