from django.shortcuts import render, redirect

# Create your views here.

def redirection(request):
    return redirect('list_targeting:index')

def index(request):
    return render(request, 'app/home.html')

def list_targeting(request):
    if request.method == 'POST':
        print(request.POST)
        if request.POST.get('action') == 'save':
            # Handle the save action
            pass
        elif request.POST.get('action') == 'submit':
            # Handle the submit action
            pass

        return redirect('list_targeting:list_targeting')

    return render(request, 'app/list-targeting.html')


def criteria_targeting(request):
    return render(request, 'app/criteria-targeting.html')