from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

class UserForm(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model=User
        fields= ['username', 'email', 'password']

class EditProfileForm(UserChangeForm):

    def __init__(self, *args, **kwargs):
        super(EditProfileForm, self).__init__(*args, **kwargs)
        del self.fields['password']
    class Meta:
        model=User
        fields=(
            'email',
            'username',
            'password'
        )