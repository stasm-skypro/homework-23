from django import forms
from catalog.models import Contact


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ["first_name", "phone", "message"]
        widgets = {
            "first_name": forms.TextInput(attrs={"class": "form-control", "placeholder": "Ваше имя"}),
            "phone": forms.TextInput(attrs={"class": "form-control", "placeholder": "Контактный телефон"}),
            "message": forms.Textarea(attrs={"class": "form-control", "placeholder": "Сообщение"}),
        }
