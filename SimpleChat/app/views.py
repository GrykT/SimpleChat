from django.shortcuts import render, redirect, get_object_or_404

from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

from django.views.generic import ListView,CreateView
from django.views.generic.edit import CreateView
from django.contrib import messages  # メッセージフレームワーク

from django.shortcuts import render,redirect
from django.http import HttpRequest
from django.template import RequestContext
from datetime import datetime

from .models import Talk, Users
from .forms import TalkForm,UsersForm

# Create your views here.
SESSION_KEY_ID = 'id'
SESSION_KEY_NAME = 'name'

def index(request):
            
            return render(
                request,
                "app/index.html",
                {
                    'content': "かくにんにすぎない"
                }
)

def reload(request):
#    if(request.session[SESSION_KEY_ID])
        #セッションがあるあいだは有効
    return redirect('room/')

def exit(request):
    if(request.session[SESSION_KEY_ID]):
        exit_user_id = request.session[SESSION_KEY_ID]
        #退室してきた場合は入退室状態を退室（2)に
        exit_user = Users.objects.get(id=exit_user_id, isInsite=1)
        exit_user.isInsite=2
        exit_user.save()
    return redirect('/')

class UsersCreateView(CreateView):
    model = Users
    form_class = UsersForm
    success_url = reverse_lazy('room')
    
    def form_valid(self, form):
        self.request.session[SESSION_KEY_ID] = self.request.POST['id']
        self.request.session[SESSION_KEY_NAME] = self.request.POST['name']

        return super().form_valid(form)

    def form_invalid(self, form):
        messages.warning(self.request, "入室できませんでした")
        return super().form_invalid(form)



class TalkCreateView(CreateView):
    model = Talk
    form_class = TalkForm
    success_url = reverse_lazy('room')
    
    title = "でんでんでんででん"

    def form_valid(self, form):
        form.instance.user_id =  Users.objects.get(
                                    id=self.request.session[SESSION_KEY_ID]
                                  , isInsite=1)
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
       context = super().get_context_data(**kwargs)
       context['talk_list'] = Talk.objects.select_related() \
                                  .all().order_by('-talk_datetime')[:20]
       context['insite_users'] = Users.objects.filter(isInsite=1)
       return context
    