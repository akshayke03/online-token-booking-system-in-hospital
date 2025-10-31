from django import forms
from django.core.validators import RegexValidator
from .models import Booking
from django.contrib.auth.models import User

class DateInput(forms.DateInput):
    input_type = 'date'

class BookingForm(forms.ModelForm):
    p_phone = forms.CharField(
        max_length=10,
        validators=[
            RegexValidator(
                regex='^[0-9]{10}$',
                message='Phone number must be 10 digits',
                code='invalid_phone_number'
            )
        ],
    )

    class Meta:
        model = Booking
        
        widgets = {
            'booking_date': DateInput(),
        }
        labels = {
            'username': "User Name",
            'p_name': "Patient Name",
            'p_phone': " Phone",
            'p_email': "Patient Email ",
            'doc_name': "Doctor Name ",
        }
        exclude = ('updated', 'created')

    def _init_(self, *args, **kwargs):
        super(BookingForm, self)._init_(*args, **kwargs)
        
        self.fields['p_email'].widget.attrs.update({
            # 'readonly':'True',
            # 'id': 'em',
            "class": " form-control"
        }),
        self.fields['booking_date'].widget.attrs.update({
            'booking_date': 'DateField()',
            'placeholder': '2023-03-15',
            "class": " form-control"
        }),
        self.fields['p_name'].widget.attrs.update({
            "class": " form-control"
        }),
        self.fields['p_phone'].widget.attrs.update({
            "class": " form-control"
        }),
        self.fields['doc_name'].widget.attrs.update({
            "class": " form-control"
        }),
        self.fields['booking_date'].widget.attrs.update({
            "class": " form-control"
        })







