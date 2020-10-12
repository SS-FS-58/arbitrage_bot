from django.contrib import admin

from .models import Exchange, Spread

# Register your models here.
admin.site.register(Exchange)
admin.site.register(Spread)
