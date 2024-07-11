from django import forms
from medicoapp.models import Application

class ApplicationForm(forms.ModelForm):
    class Meta:
        model = Application
        fields =['name','email','phone','AppointmentDate','Department','Doctor','message']