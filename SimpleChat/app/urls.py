from django.urls import path

#from .views import ...
from .views import get

urlpatterns = [
    path('index',get,name='sample'),
]