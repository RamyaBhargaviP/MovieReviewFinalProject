from django.shortcuts import render
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
# Create your views here
from .forms import SearchMovieForm
from .forms import SignUpForm
import requests

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request,user)
            return redirect('login')
    else:
        form = SignUpForm()
    return render(request, template_name='signup.html', context = {'form': form})

@login_required(login_url = 'login')
def search(request):
    if request.method == 'POST':
        form = SearchMovieForm(request.POST)
        if form.is_valid():
            movie_title = form.cleaned_data['movie_title']
            response = requests.get('https://www.omdbapi.com/?t=%s&apikey=4a57fce' % movie_title)
            res = response.json()
            print(res)
            return render(request, template_name = 'result.html', context = {
                'Title':res['Title'],
                'poster':res['Poster'],
                'plot':res['Plot'],
                'imdbrating': res['imdbRating'],
                'Actors':res['Actors'],
                'Released':res['Released'],
                'lang':res['Language'],
                'Dir':res['Director']
            })
    else:
        form = SearchMovieForm()
        return render(request,template_name = 'searchpage.html', context = {'form': form})