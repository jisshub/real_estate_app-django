from django.http import request
from django.shortcuts import render

from .models import Listing


# Create your views here.
def index(request):
    # fetch all objects
    listings = Listing.objects.all()
    # pass it to a dictionary
    context = {
        'listing': listings
    }
    # render html and pass the dictionary as argument
    return render(request, 'listings/listings.html', context)


def listing(request, listing_id):
    # listing_id parameter given in listing url in urls.py file
    return render(request, 'listings/listing.html')


def search(request):
    return render(request, 'listings/search.html')
