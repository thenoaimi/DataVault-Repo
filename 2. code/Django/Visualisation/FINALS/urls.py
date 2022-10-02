from django.contrib import admin
from django.conf import settings
from django.urls import path, include
from login import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', views.index),
    path('login/', views.login),
    path('logout/', views.logout),
    path('TEST/',include('TEST.urls'))
]