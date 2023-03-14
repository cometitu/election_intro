from django.shortcuts import render, redirect
from django.db.models import F
import random
from .models import Website

# Create your views here.
def home(request):
    #urls = ["http://www.google.dk", "http://www.google.com", "http://www.yahoo.com", "https://res50.itu.dk/helios/e/boardelections/vote"]
    urls = Website.objects.all().filter(total_count__lte=100)
    if urls:
        urlselected = random.choice(urls)
        urls.filter(url_name =urlselected).update(total_count = F("total_count") + 1)
    else:
        urlselected = "Admin"
        
    context ={   
        "urlselected" : urlselected,
        #"urlselected" : 'http://www.' + urlselected,
    }

    return render(request, 'mainapp/index.html', context)


def vote(request):
    urls = ["http://www.google.dk", "http://www.google.com", "http://www.yahoo.com", "https://res50.itu.dk/helios/e/boardelections/vote"]
    urlselected = random.choice(urls)
    return redirect(urlselected)   
    #return redirect('http://www.'+ urlselected) 