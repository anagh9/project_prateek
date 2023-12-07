from django.shortcuts import render, redirect

# Create your views here.

def redirection(request):
    return redirect('list_targeting:index')

def index(request):
    return render(request, 'app/home.html')

def list_targeting(request):
    return render(request, 'app/list-targeting.html')


def criteria_targeting(request):
    return render(request, 'app/criteria-targeting.html')