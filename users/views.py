from django.shortcuts import  redirect, render
# Create your views here.
from .forms import RegisterForm
from home.forms import Post
from django.contrib.auth import login

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home:homepage')

    else:
        form = RegisterForm()

    return render(request, 'registration/register.html', {'form': form})
