from django.shortcuts import render
from django.http import HttpResponse
from listings.models import Listing
from realtors.models import Realtor

# Create your views here.
def index(request):
    listing = Listing.objects.order_by('-list_date').exclude(is_published=False)[:1]
    context = {
        "listings" : listing
    }
    return render(request, 'index.html', context)


def about(request):
    realtor = Realtor.objects.all()
    context = dict(realtors=realtor)
    return render(request, 'about.html', context)
