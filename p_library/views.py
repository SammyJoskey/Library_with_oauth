from django.http import HttpResponse
from django.http.response import HttpResponseRedirect
from django.template import loader
from django.shortcuts import redirect, render

from django.contrib import auth
from django.contrib.auth.forms import AuthenticationForm 

from django.urls import reverse_lazy
from django.forms import formset_factory  

from .models import Book, Author, Publisher, Friend
from .forms import AuthorForm, BookForm, FriendForm

from django.views.generic import CreateView, ListView, FormView
from django.views.generic.edit import FormView, CreateView, DeleteView, UpdateView

from django.contrib.auth.forms import UserCreationForm  
from django.contrib.auth import login, authenticate  
from .forms import UserProfileForm  
from .models import UserProfile

from allauth.socialaccount.models import SocialAccount

def index(request):  
    

    template = loader.get_template('home.html')
    books = Book.objects.all()
    biblio_data = {
        "title": "мою библиотеку",
        "books": books,
    }
    context = {}  
    if request.user.is_authenticated:  
        context['username'] = request.user.username  
    return HttpResponse(template.render(biblio_data, request))


class BookEdit(CreateView):  
    model = Book  
    form_class = BookForm  
    success_url = reverse_lazy('book_list') 
    template_name = 'book_add.html'

class BookList (ListView):  
    model = Book  
    template_name = 'book_list.html'
    context_object_name = 'book_list'


class AuthorEdit(CreateView):  
    model = Author  
    form_class = AuthorForm  
    success_url = reverse_lazy('p.library:author_list')
    template_name = 'authors_add.html'

class AuthorList (ListView):  
    model = Author  
    template_name = 'author_list.html'
    context_object_name = 'author_list'


class FriendEdit(CreateView):
    model = Friend
    form_class = FriendForm
    success_url = reverse_lazy('p.library:friend_list')
    template_name = 'friend_add.html'


class FriendList (ListView):  
    model = Friend
    template_name = 'friend_list.html'
    context_object_name = 'friend_list'


class PublisherList (ListView):  
    model = Publisher
    template_name = 'publisher_list.html'
    context_object_name = 'publisher_list'


def signin(request):
    context = {}
    if request.user.is_authenticated:
        context['username'] = request.user.username
        # сначала читаем таблицу профилей своих пользователей
        request_user_profile = UserProfile.objects.filter(
            user=request.user).first()
        if request_user_profile:
            context['auth_type'] = 1
            context['age'] = request_user_profile.age
        else:
            context['auth_type'] = 2
            context['github_url'] = SocialAccount.objects.get(
                provider='github', user=request.user).extra_data['html_url']
            context['public_repos'] = SocialAccount.objects.get(
                provider='github', user=request.user).extra_data['public_repos']
            context['created_at'] = SocialAccount.objects.get(
                provider='github', user=request.user).extra_data['created_at']

    return render(request, 'index.html', context)


def signup(request):
    if request.method == 'POST':
        form = UserProfileForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = UserProfileForm()
    return render(request, 'register.html', {'form': form})