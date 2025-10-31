from django.db import models
from django.contrib.auth.models import User

class Token(models.Model):
    name = models.CharField(max_length=100)
    # Other fields...

class BookingSlot(models.Model):
    token = models.ForeignKey(Token, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    # Other fields...
class Doctors(models.Model):
    doc_name = models.CharField(max_length=220)
    doc_spec = models.CharField(max_length=220)
   
    doc_image = models.ImageField(upload_to='doctors')

    def __str__(self):
        return 'DR.'+self.doc_name +' - '+'('+self.doc_spec +')'

    
class Booking (models.Model):
    username= models.CharField(max_length=225)  
    p_name = models.CharField(max_length=225)
    p_phone = models.CharField(max_length=225)
    p_email =models.EmailField()
    doc_name =  models.ForeignKey(Doctors, on_delete=models.CASCADE)
    booking_date = models.DateField()
    booked_on = models.DateField(auto_now=True)
