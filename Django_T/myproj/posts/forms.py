from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)
    age = forms.IntegerField()
    gender = forms.ChoiceField(choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')])

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'age', 'gender', 'password1', 'password2']