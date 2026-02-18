from django import forms
from .models import Service, Booking


class ServiceForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = ['name', 'category', 'providers', 'status', 'price', 'description']
        widgets = {
            'providers': forms.CheckboxSelectMultiple(),
        }


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['customer', 'service', 'provider', 'service_date', 'status']
        widgets = {
            'service_date': forms.DateInput(attrs={'type': 'date'}),
        }
