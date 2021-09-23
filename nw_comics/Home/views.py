from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# Create your views here.

def index(request):
    slide1 = {
        'url' : 'the_witcher.jpg',
        'nome' : 'The Witcher'
    }
    slide2 = {
        'url' : 'stranger_things.jpeg',
        'nome' : 'Stranger Things'
    }
    slide3 = {
        'url' : 'the_100.jpg',
        'nome' : 'The 100'
    }

    context = {
        'slide1' : slide1,
        'slide2' : slide2,
        'slide3' : slide3
    }
    return render(request, 'home.html', context=context)