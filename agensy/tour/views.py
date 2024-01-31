from django.shortcuts import render, redirect
from .models import *
from .forms import *
# Create your views here.


navlinks = [
    {
        'title':'Главная',
        'link': 'index',
    },
    {
        'title':'О нас',
        'link':'about'
    },
    {
        'title':'Туры',
        'link':'tours'
    },
    {
        'title':'Контакт',
        'link':'contact'
    }
]

def index(request):
    tours = Tours.objects.all()
    context = {
        'tours': tours,
        'nav': navlinks,
        'active': navlinks[0]['title']
    }
    return render(request, 'tour/index.html', context)

def about(request):
    context = {
        'white': True,
        'nav': navlinks,
        'active': navlinks[1]['title']
    }
    return render(request, 'tour/about.html', context)

def contact(request):
    context={
        'nav': navlinks,
        'active': navlinks[3]['title'],
        'white': True,

    }
    return render(request, 'tour/contact.html',context)

def tours(request):
    tours = Tours.objects.all()
    context = {
        'white': True,
        'tours': tours,
        'nav': navlinks,
        'active': navlinks[2]['title']
    }
    return render(request, 'tour/tours.html', context)

def info(request, slug):
    tour = Tours.objects.get(slug=slug)
    context = {
        'tour': tour,
        'white': True,
        'nav': navlinks,
        'active': navlinks[2]['title']
    }
    return render(request, 'tour/info_tour.html', context)


def contact_form(request):
    if request.method == 'POST':
        print("Hello there2")
        form = ContactForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')

        else:
            print(f"error here \n {request}")
    else:
        form = ContactForm()

    return render(request, 'website/contact.html', {'form': form})