from .models import *
from django import forms

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking_tour
        fields = ('name', 'number', 'ot', 'do',)


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ('first_name', 'last_name', 'email', 'phone', 'message', )