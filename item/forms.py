from django import forms
from .models import Contact


# class ContactForm(forms.Form):
#     yourname = forms.CharField(max_length=5, label='Your Name')
#     mailid = forms.EmailField(label='e-mail')
#     subject = forms.CharField(label="Subject", max_length=5)
#     body = forms.CharField(max_length=5)


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        # fields = "__all__"
        fields = ['yourname','mailid','subject','body']
