from django.shortcuts import render, redirect
from .forms import RegisterForm

def index_view(request, *args, **kwargs):
    return render(request, 'login/index.html', {
        'user': request.user,
    })

def register_view(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = RegisterForm()
    return render(request, 'login/register.html', {'form': form})
