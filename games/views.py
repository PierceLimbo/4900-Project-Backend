from django.shortcuts import render

def backend_home(request):
    return render(request, 'backend_home.html')
