from django.shortcuts import render

def homepage(request):
    return render(request, 'home_app/home.html')
