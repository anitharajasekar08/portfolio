from django import forms
from .models import Contact

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'number', 'content']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Your Name'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Your Email'}),
            'number': forms.TextInput(attrs={'placeholder': 'Your Phone'}),
            'content': forms.Textarea(attrs={'placeholder': 'Your Message', 'rows': 5}),
        }

    def clean_name(self):
        name = self.cleaned_data.get('name')
        if len(name) < 2:
            raise forms.ValidationError("Name must be at least 2 characters.")
        return name

    def clean_number(self):
        number = self.cleaned_data.get('number')
        if not number.isdigit():
            raise forms.ValidationError("Phone number must contain only digits.")
        if len(number) < 10:
            raise forms.ValidationError("Phone number must be at least 10 digits.")
        return number