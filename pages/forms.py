from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column

class ContactForm(forms.Form):
    name = forms.CharField(required=True, widget=forms.TextInput(attrs={'placeholder': 'Your Name'}))
    email = forms.EmailField(required=True, widget=forms.TextInput(attrs={'placeholder': 'Your Email'}))
    company = forms.CharField(required=True, label='Company Name', widget=forms.TextInput(attrs={'placeholder': 'Company Name'}))
    phone = forms.CharField(required=True, label='Phone Number', widget=forms.TextInput(attrs={'placeholder': 'Phone Number'}))
    message = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Message'}), required=True, label='Message')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_show_labels = False

class QuoteForm(forms.Form):
    name = forms.CharField(required=True, widget=forms.TextInput(attrs={'placeholder': 'Your Name'}))
    email = forms.EmailField(required=True, widget=forms.TextInput(attrs={'placeholder': 'Your Email'}))
    company = forms.CharField(required=True, label='Company Name', widget=forms.TextInput(attrs={'placeholder': 'Company Name'}))
    phone = forms.CharField(required=True, label='Phone Number', widget=forms.TextInput(attrs={'placeholder': 'Phone Number'}))
    message = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Message'}), required=True, label='Message')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_show_labels = False