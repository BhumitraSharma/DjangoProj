from django.contrib import admin
from .models import Listing


class ListingAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'is_published', 'price')
    list_display_links = ('id', 'title', 'price')
    list_editable = ('is_published',)
    list_per_page = 20


admin.site.register(Listing, ListingAdmin)
