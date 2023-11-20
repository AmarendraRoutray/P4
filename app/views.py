from django.shortcuts import render

# Create your views here.

def redg(request):
    return render(request, 'registration.html')