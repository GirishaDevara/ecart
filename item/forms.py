from django import forms


class ContactForm(forms.Form):
    yourname = forms.CharField(max_length=5, label='Your Name')
    mailid = forms.EmailField(label='e-mail')
    subject = forms.CharField(label="Subject", max_length=5)
    body = forms.CharField(max_length=5)
