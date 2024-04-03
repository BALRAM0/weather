from .import views
from django.contrib import admin
from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path('',views.main,name='index'),
    path('about',views.about,name='about'),
    path('main',views.main,name='index'),
    path('ai',views.ai,name='ai'),
    path('result',views.ai,name='ai'),
    
]+static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)