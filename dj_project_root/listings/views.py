from django.http import request
from django.shortcuts import render

from .models import Listing


# Create your views here.
def index(request):
    each_listing = Listing.objects.all()
    list_dict = {'list': each_listing}
    return render(request, 'listings/listings.html', list_dict)


def listing(request):
    return render(request, 'listings/listing.html')


def search(request):
    return render(request, 'listings/search.html')
