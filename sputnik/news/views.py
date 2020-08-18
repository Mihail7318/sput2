from django.shortcuts import render
from .models import article


def news(request):
    articles = article.objects.order_by('-date')
    return render(request, "news.html", {'articels': articles})


# Create your views here.
def news_prev(request, pk):
    news = article.objects.filter(id=pk)
    return render(request, "detail_news.html", {'data': news})
