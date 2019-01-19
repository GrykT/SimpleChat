from django.shortcuts import render, redirect, get_object_or_404

from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

from django.views.generic import ListView,CreateView
from django.views.generic.edit import CreateView
from django.contrib import messages  # メッセージフレームワーク

from django.shortcuts import render
from django.http import HttpRequest
from django.template import RequestContext
from datetime import datetime

from .models import Talk, Users
from .forms import TalkForm,UsersForm

# Create your views here.
def index(request):
            
            return render(
                request,
                "app/index.html",
                {
                    'content': "かくにんにすぎない"
                }
)

class UsersCreateView(CreateView):
    model = Users
    form_class = UsersForm
    success_url = reverse_lazy('room')
    
    def form_valid(self, form):
        self.request.session['user_name'] = self.request.POST
        return super().form_valid(form)

    def form_invalid(self, form):
        return super().form_invalid(form)

class TalkCreateView(CreateView):
    model = Talk
    form_class = TalkForm
    
    title = "でんでんでんででん"

   # def get_context_data(self, **kwargs):
   #     context = super().get_context_data(**kwargs) # はじめに継承元のメソッドを呼び出す
   #     return context
    
 
class TalkListView(ListView):
    model = Talk
    title = "部屋"