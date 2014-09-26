from django.contrib import admin
from .models import Zipcode, City, Address


admin.site.register(Zipcode)
admin.site.register(City)
admin.site.register(Address)
