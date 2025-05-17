#This file defines a Django form (ComplaintForm) to handle user input for complaints.


from django import forms# Provides Django’s form functionalities.
from .models import Complaint#This form is based on the Complaint model.

class ComplaintForm(forms.ModelForm):
    class Meta:
        model = Complaint#Links the form to the Complaint model.
        fields = ['title', 'description']#Specifies which fields to include in the form (title, description).
        widgets = {#Widgets customize how form fields appear in the HTML template.
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),#rows=5 → Sets the height of the description text area.
        }