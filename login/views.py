from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.contrib.auth import authenticate, login

def index_view(request, *args, **kwargs):
    return render(request, 'login/index.html', {
        'user': request.user,
    })

def register_view(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()

            new_user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password1'],
            )
            login(request, new_user)

            return redirect('/')
    else:
        form = RegisterForm()
    return render(request, 'login/register.html', {'form': form})
