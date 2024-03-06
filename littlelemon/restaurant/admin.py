from django.contrib import admin

# Register your models here.
from .models import Booking_Table
from .models import Menu_Table


admin.site.register(Booking_Table)
admin.site.register(Menu_Table)