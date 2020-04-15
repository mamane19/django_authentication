from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

def index(request):
    users = User.objects.count()
    return render(request, 'core/index.html', {'users':users})

def signup(request):
    if request.method=='POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            print('valid')
            form.save()
            return redirect('home')
        else:
            print('Not valid')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form':form})

@login_required
def secret_page(request):
    return render(request, 'core/secret_page.html')