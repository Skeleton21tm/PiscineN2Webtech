from django.shortcuts import render
import datetime

def home(request):
    current_year = datetime.datetime.now().year
    return render(request, 'home/home.html', {'current_year': current_year})



