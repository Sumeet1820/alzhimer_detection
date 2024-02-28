from django.conf.urls import url, include
from . import views
from django.urls import path

urlpatterns = [
    url(r'^accounts/', include('allauth.urls')),
    path('base/',views.base,name='base')

]
