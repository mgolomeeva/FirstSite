from django.http import Http404
from django.shortcuts import render_to_response
from models import Quote
from random import randint
from models import Category
from django.shortcuts import get_object_or_404
from django.http import HttpResponse


def GetRandomQuote(quotes):
    range = quotes.count()
    index = randint(0,range-1)
    return quotes[index]


def home(request): #comes from the browser
    quotes = Quote.objects.all() #gets all quotes from database
    data = {}
    data['random_quote'] = GetRandomQuote(quotes)
    data["categories"] = Category.objects.all()
    return render_to_response('quote.html', data)


def single_category(request, url_name): # comes from the browser
    data = {}
    # data["categories"] = Category.objects.all()
    cat = data['cat'] = get_object_or_404(Category, name__iexact=url_name)
    quotes = data['quotes'] = Quote.objects.filter(category=cat)
    return render_to_response('single_category.html', data)


def index(request):
    return HttpResponse("We provide you with daily inspiration. Get your qotd")
