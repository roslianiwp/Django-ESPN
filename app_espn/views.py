from django.shortcuts import render, redirect, get_object_or_404
from .forms import KomenForm, LikeForm, Search
from .models import Kategori, UserNetijen, UserWartawan, Artikel, Komen, Like
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.views.generic import ListView
from django.db.models import Q

# Create your views here.

def artikel(request):
    artikels = Artikel.objects.all()
    paginator = Paginator(artikels,3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'artikel.html',{'page_obj':page_obj})

class SearchResultsView(ListView):
    model = Artikel
    template_name = 'search.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        object_list = Artikel.objects.filter(
            Q(judul__icontains=query) | Q(kategori_artikel__kategori_artikel__icontains=query)
        )
        return object_list

def home(request):
    return render(request, 'index_espn.html')

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            # login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form_signup': form})

def login(request):
    return render(request, 'login.html')

def artikel_detail(request, artikel_id):
    artikels = get_object_or_404(Artikel, pk=artikel_id)
    user = get_object_or_404(UserNetijen, pk=1)
    if request.method =='POST':
        cm = Komen.objects.create(
            artikel = artikels,
            netizen = user,
            komen = request.POST.get('commenttt'),
            tgl_komen = '2020-04-10',
        )
        cm.save()
    return render(request, 'detail_artikel.html', {'artikels':artikels, 'post_active':True})

def artikel_detail_add_like(request, artikel_id):
    artikels = get_object_or_404(Artikel, pk=artikel_id)
    cl = artikels.clap
    Artikel.objects.filter(pk=artikel_id).update(clap=cl+1)
    return redirect('/artikel/'+str(artikel_id)+'/')

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