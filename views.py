from django.contrib import messages
from django.shortcuts import render,redirect
from .forms import BookingForm

def booking(request):

    if request.method == "POST":
       form =BookingForm(request.POST)

       if form .is_valid():
           form.save()
           return render(request, 'confirmation.html')
       else:
          messages.info(request,'booking failed ')
          return redirect('booking')
    
    form = BookingForm()
    dict_form ={
        'form' : form
    }
    return render(request, 'booking.html',dict_form)
                  