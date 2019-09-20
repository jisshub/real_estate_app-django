from django.contrib import admin

from .models import Listing


# to change the look of Listing page in admin area
class ListingAdmin(admin.ModelAdmin):
    # pass the fields to be displayed om the page
    list_display = ['id', 'title', 'price', 'is_published', 'list_date', 'realtor']
    # to display the links for the fields we want.
    list_display_links = ['title']
    # # to make thr realtors as a filter box, thus v can thru each realtor
    list_filter = ['realtor']
    # # to set this_published field as editable one, thus a checkbox is shown there.
    list_editable = ['is_published']
    # # search thru the listings, here v search using title field
    search_fields = ['title']
    # # to show no of listings shud appear on a single page
    list_per_page = 3


# Register your models here.
admin.site.register(Listing, ListingAdmin)
