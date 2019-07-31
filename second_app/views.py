from django.shortcuts import render

# Create your views here.

from .models import Portfolio

def portfolio(request):

    folfol = Portfolio.objects

    return render(request, 'portfolio.html', 
    { 'popo' : folfol} )