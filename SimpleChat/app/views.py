from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from django.views.generic import ListView,CreateView

from django.shortcuts import render,redirect
from .models import Talk, Users
from .forms import TalkForm,UsersForm

# Create your views here.
SESSION_KEY_ID = 'id'
SESSION_KEY_NAME = 'name'

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



class TalkCreateView(CreateView):
    model = Talk
    form_class = TalkForm
    success_url = reverse_lazy('room')
    
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
    