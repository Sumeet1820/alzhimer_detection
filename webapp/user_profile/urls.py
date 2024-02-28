from django.conf.urls import url, include
from . import views
from .views import home2
from django.urls import path

urlpatterns = [
    url(r'^accounts/profile/$', views.UserProfileView.as_view(), name="profile"),
    url(r'^accounts/status/$', views.UserStatusView.as_view(), name="status"),
    path('home2/', home2, name='home2'),
    path('',views.index,name='index'),
    path('addetect',views.addetect,name='addetect'),
]
