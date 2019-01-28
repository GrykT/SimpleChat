from django.urls import path

#from .views import ...
from .views import index,exit,UsersCreateView,TalkCreateView


urlpatterns = [
    path('', UsersCreateView.as_view() , name='talk'),
    path('room/', TalkCreateView.as_view() , name='room'),
    path('exit', exit , name='exit'),
    path('index',index,name='talk'),
]