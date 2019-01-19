from django.urls import path

#from .views import ...
from .views import index,UsersCreateView,TalkCreateView,TalkListView


urlpatterns = [
    path('', UsersCreateView.as_view() , name='talk'),
    path('room/', TalkCreateView.as_view() , name='room'),
    path('index',index,name='sample'),
]