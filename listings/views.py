from django.shortcuts import render


def index(request):
    return render(request, 'listing/listings.html')


def list(request):
    return render(request, 'listing/list.html')


def search(request):
    return render(request, 'listing/search.html')
