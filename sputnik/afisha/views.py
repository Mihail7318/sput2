from django.shortcuts import render
from .models import afisha
# Create your views here.

def afisha_detail(request):
    films = afisha.objects.order_by('-date')
    return render(request, "afisha-s.html", {'films': films})

