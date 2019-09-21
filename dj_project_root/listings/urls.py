from . import views
from django.urls import path

urlpatterns = [
    # for listings page
    path('', views.index, name='listings'),
    # for each single listings. v need to include an id for each listing..
    # eg, listings/23. for that v use a parameter called listing_id,
    path('<int: listing_id>', views.listing, name='listing'),
    # here int is the type of parameter. <int: listing_id> is the way to access the id from the view
    # method.
    path('search/', views.search, name='search'),

]
