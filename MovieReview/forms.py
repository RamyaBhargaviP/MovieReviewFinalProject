from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length = 30, help_text = 'Required. Enter the Valid Email')

    class Meta:
        model = User
        fields = ['username','email','password1','password2']

class SearchMovieForm(forms.Form):
    movie_title = forms.CharField(max_length = 100,widget=forms.TextInput(attrs={'placeholder': 'Enter movie'}))