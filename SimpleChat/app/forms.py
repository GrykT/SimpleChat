"""
Definition of forms.
"""

from .models import Talk
from .models import Users

from django import forms

class UsersForm(forms.ModelForm):
    class Meta:
        model = Users
        fields = ('id','name',)
        widget = {
                    'id':forms.TextInput(),
                    'name': forms.TextInput(),
            }

    def save(self):
        my_id = self.cleaned_data['id']
        exist_user = Users.objects.filter(id=my_id, isInsite=2)
        if exist_user.exists():
            #もう名前があるユーザーは追加しない
            insite_user = Users.objects.get(id=my_id)
            self.instance = insite_user
            self.instance.name = self.cleaned_data['name'] #名前も

        self.instance.isInsite = 1
        self.instance.save()
        return self.instance

    #def clean_id(self):
    #    my_id = self.cleaned_data['id']
    #    if Users.objects.filter(id=my_id,isInsite=1).exists():
    #         raise forms.ValidationError('入室済みのユーザーです')
    #    return my_id

    def clean(self):
        my_id = self.cleaned_data['id']
        if Users.objects.filter(id=my_id,isInsite=1).exists():
             raise forms.ValidationError('入室済みのユーザーです')
        

class TalkForm(forms.ModelForm):
    class Meta:
        model = Talk
        fields = ('talk_text',)      
        widgets = {
            'talk_text':forms.Textarea(attrs={'rows':2,'cols':40})
            }
