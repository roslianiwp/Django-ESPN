from django.shortcuts import render, redirect
from .forms import KomenForm, LikeForm
from .models import Kategori, UserNetijen, UserWartawan, Artikel, Komen, Like
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect


# Create your views here.
# def index(request):
#     return render(request, 'index_espn.html')

def artikel(request):
    artikels = Artikel.objects.all()
    # if request.method == 'POST':
    #     form = KomenForm(request.POST)
    #     if form.is_valid():
    #         form.save()
    #         return redirect('artikel')
    # else:
    #     form = KomenForm()

    # if request.method == 'POST':
    #     form_like = LikeForm(request.POST)
    #     if form_like.is_valid():
    #         form_like.save()
    #         return redirect('artikel')
    # else:
        # form_like = LikeForm()

    return render(request, 'artikel.html',{'artikels': artikels
    # , 'form': form, 'form_like':form_like
    })


# BUAT SEARCH
# def index(request):
#     query_list = Artikel.objects.all()
#     query = request.GET.get('Title')
#     if query:
#         query_list = query_list.filter(judul__icontains=query)
    
#     return render(request, 'index_espn.html', {'query': query_list})




def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form_signup': form})
def home(request):
    return render(request, 'index_espn.html')

def football(request):
    return render(request, 'football.html')

def nba(request):
    return render(request, 'NBA.html')

def nfl(request):
    return render(request, 'NFL.html')

def cricket(request):
    return render(request, 'Cricket.html')

def rugby(request):
    return render(request, 'Rugby.html')

def golf(request):
    return render(request, 'golf.html')