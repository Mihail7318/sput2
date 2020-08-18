from django.shortcuts import render
from .models import event, PostsImages
from django.db.models import F


# Create your views here.
def events(request):
    events = event.objects.order_by('-date')
    # images = PostsImages.objects.filter(event__id=F('event__id'))
    # images = event.images.all()
    return render(request, "events.html", {'events': events})


def events_prev(request, pk):
    event_detail = event.objects.filter(id=pk)
    return render(request, "detail.html",{"data":event_detail})
