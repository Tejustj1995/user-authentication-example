from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


# Create your views here.
def index(request):
    return render(request, 'authusers/index.html')


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            password
            user = authenticate(username=username, password=password)
            login(request)
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            else:
                return redirect('index')
        else:
            form = UserCreationForm()
        return render(request, 'registration/registration.html', {'form': form})
    return render(request, 'registration/registration.html')


def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
        else:
            form = AuthenticationForm()
    return render(request, 'registration/login.html', {'form': form})
