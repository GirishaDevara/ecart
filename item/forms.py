from django import forms


class ContactForm(forms.Form):
    mailid = forms.EmailField()
    subject = forms.CharField(label="Subject", max_length=100)
    body = forms.CharField(widget=forms.Textarea)
