# projeto/views.py
from datetime import datetime

from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    now = datetime.now()
    context = {
        'current_time': now
    }
    return render(request, 'index.html', context)