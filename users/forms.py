from django import forms
from .models import Profile

class ProfileModelForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('first_name', 'last_name',  'username')

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = Profile
        fields = ['username', 'email', 'phone', 'address', 'last_name', 'first_name']