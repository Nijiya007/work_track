from django import forms
from .models import Apply,FuelCharge

class AppliedServiceForm(forms.ModelForm):
    class Meta:
        model = Apply
        photos_of_item = forms.FileField(
        widget=forms.ClearableFileInput(attrs={'multiple': True}), 
        required=False
    )
        fields = [
            'customer', 'name', 'address', 'contact_number', 'whatsapp_number', 'referred_by',
            'service_by', 'work_type', 'item_name_or_number', 'issue', 'photos_of_item',
            'estimation_document', 'estimated_price', 'estimated_date', 'any_other_comments'
        ]



class FuelChargeForm(forms.ModelForm):
    class Meta:
        model = FuelCharge
        fields = ['technician_name', 'date', 'purpose', 'kilometers', 'cost']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'technician_name': forms.TextInput(attrs={'readonly': True}),
        }

