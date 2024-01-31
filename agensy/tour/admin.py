from django.contrib import admin
from .models import *

class PhotoInline(admin.TabularInline):
    model = Photos
    extra = 3




class ToursAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'days', 'everyday',)
    list_display_links = ('name',)
    list_editable = ('price', 'days', 'everyday',)
    list_filter = ('name', 'price', 'days',)

    prepopulated_fields = {'slug': ('name',)}
    inlines = [PhotoInline]


admin.site.register(Tours, ToursAdmin)

