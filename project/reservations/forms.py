from django import forms

from .models import *
from users.models import CustomUser

class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ['doctor', 'service', 'date', 'start_time', 'description']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'start_time': forms.Select(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['doctor'].widget.attrs['disabled'] = True
        self.fields['date'].widget.attrs['disabled'] = True
        self.fields['start_time'].widget.attrs['disabled'] = True
        self.fields['description'].widget.attrs['placeholder'] = 'Here you can add your symptoms or any other information you want to share with the doctor.'
        self.fields['description'].required = False

        # Labels
        self.fields['doctor'].label = 'Doctor (Required)'
        self.fields['service'].label = 'Service (Required)'
        self.fields['date'].label = 'Date (Required)'
        self.fields['start_time'].label = 'Start Time (Required)'
        self.fields['description'].label = 'Description (Optional)'

        self.fields['doctor'].queryset = CustomUser.objects.none()

        # If the form is bound, set the choices for the doctor field
        if self.is_bound:
            doctor_id = self.data.get('doctor')
            if doctor_id:
                try:
                    doctor = CustomUser.objects.get(id=doctor_id)
                    self.fields['doctor'].queryset = CustomUser.objects.filter(id=doctor_id)
                except CustomUser.DoesNotExist:
                    pass