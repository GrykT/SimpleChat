"""
Definition of forms.
"""

from .models import Talk
from .models import Users

from django import forms

class UsersForm(forms.ModelForm):

    class Meta:
        model = Users
        fields = ('name',)
        widget = {
                    'name': forms.TextInput(),
            }

class TalkForm(forms.ModelForm):
    class Meta:
        model = Talk
        fields = ('talk_text',)
        widget = {
                    'talk_text':forms.Textarea(attrs={'rows':30}),
            }