from django.shortcuts import render
from .forms import RegisterForm
from .models import Register
import random


# Create your views here.

def home(request):
    form = RegisterForm()
    return render(request, 'LoginRegisterApp/index.html', {'RegisterForm': form})


def register(request):
    if request.method == 'POST':
        filled_form = RegisterForm(request.POST)
        if filled_form.is_valid():
            pass
