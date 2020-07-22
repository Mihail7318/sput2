from django.shortcuts import render
from .models import event

# Create your views here.
def events(request):
    events = event.objects.order_by('-date')
    return render(request, "events.html", {'events': events})

def events_prev(request):
    	pass    