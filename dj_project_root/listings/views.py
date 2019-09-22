from django.http import request
from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Listing


# Create your views here.
def index(request):
    # fetch all objects
    listings = Listing.objects.all()
    # create a paginator and pass the listings set and an argument
    # 3 means listings per page
    paginator = Paginator(listings, 3)
    page = request.GET.get('page')
    page_listing = paginator.get_page(page)

    # pass it to a dictionary
    context = {
        'listing': page_listing
    }
    # render html and pass the dictionary as argument
    return render(request, 'listings/listings.html', context)


def listing(request, listing_id):
    # listing_id parameter given in listing url in urls.py file

    return render(request, 'listings/listing.html')


def search(request):
    return render(request, 'listings/search.html')
