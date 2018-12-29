"""
Definition of forms.
"""

from .models import Talk
from .models import Users

from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import ugettext_lazy as _

class BootstrapAuthenticationForm(AuthenticationForm):
    """Authentication form which uses boostrap CSS."""
    username = forms.CharField(max_length=254,
                               widget=forms.TextInput({
                                   'class': 'form-control',
                                   'placeholder': 'User name'}))
    password = forms.CharField(label=_("Password"),
                               widget=forms.PasswordInput({
                                   'class': 'form-control',
                                   'placeholder':'Password'}))


class UsersForm(forms.ModelForm):
    model = Users
    fields = ('name')
    widget = {
                'name': forms.TextInput(),
        }

class TalkForm(forms.ModelForm):
    model = Talk
    fields = ('talk_text')
    widget = {
                'talk_text':forms.Textarea(attrs={'rows':4}),
        }