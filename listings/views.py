from django.core.paginator import Paginator
from django.shortcuts import render
from listings.models import Listing
from realtors.models import Realtor
def index(request):
    listings = Listing.objects.order_by('-price').exclude(is_published=False)

    paginator = Paginator(listings, 3)
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)

    context = {
        'listings' : paged_listings
    }

    return render(request, 'listing/listings.html', context)


def list(request, listing_id):
    query = Listing.objects.get(id=listing_id)

    realtor = Realtor.objects.filter(is_MVP=True)
    context = {
        'query' : query,
        'realtor': realtor,
    }
    return render(request, 'listing/list.html', context)


def search(request):
    queryset_list = Listing.objects.order_by('-list_date')
    #Keyword exits
    if 'keywords' in request.GET:
        keywords = request.GET['keywords']
        if keywords:
            queryset_list = queryset_list.filter(description__icontains=keywords)

    if 'city' in request.GET:
        keyword = request.GET['city']
        if keyword:
            queryset_list = queryset_list.filter(city = keyword)
    if 'state' in request.GET:
        keyword = request.GET['state']
        if keyword:
            queryset_list = queryset_list.filter(state = keyword)
    if 'bedrooms' in request.GET:
        keyword = request.GET['bedrooms']
        if keyword:
            queryset_list = queryset_list.filter(bedrooms = keyword)
    if 'price' in request.GET:
        keyword = int(request.GET['price'])
        if keyword:
            queryset_list = queryset_list.filter(price__lte=keyword)


    context =  {
        'listings': queryset_list,
        'values' : request.GET
    }
    return render(request, 'listing/search.html', context)
