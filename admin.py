from django.contrib import admin
from .models import Doctors,Booking
from django.contrib.auth.models import User

# Register your models here.


admin.site.register(Doctors)



class BookingAdmin(admin.ModelAdmin):
    list_display = ('id','username','p_name','p_phone','doc_name','booking_date','booked_on')

admin.site.register(Booking,BookingAdmin)