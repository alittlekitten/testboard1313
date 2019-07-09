from django.shortcuts import render
from .models import Board

# Create your views here.
def home(request):
    return render(request, 'home.html')

def check(request):
    oardbs = Board.objects
    return render(request, 'check.html',{'boards':boards})