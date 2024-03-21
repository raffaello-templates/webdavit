from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget

from .models import Post, Comment

class PostForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_show_labels = True
        self.helper.layout = Layout(
            Row(
                Column('title', css_class='form-group col-md-8 mb-0'),
                css_class='form-row'
            ),
            'content',
            Row(
                Column('publish', css_class='form-group col-md-4 mb-0'),
                Column('banner', css_class='form-group col-md-4 mb-0'),
                Column('status', css_class='form-group col-md-4 mb-0'),
                css_class='form-row'
            ),
            Submit('submit', 'Create')
        )

    class Meta:
        model = Post
        widgets = {
            'content': SummernoteWidget(),
        }
        exclude = ('author', 'slug',)


class PostUpdateForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_show_labels = True
        self.helper.layout = Layout(
            Row(
                Column('title', css_class='form-group col-md-8 mb-0'),
                css_class='form-row'
            ),
            'content',
            Row(
                Column('banner', css_class='form-group col-md-6 mb-0'),
                Column('status', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),
            Submit('submit', 'Update')
        )

    class Meta:
        model = Post
        widgets = {
            'content': SummernoteWidget(),
        }
        exclude = ('author', 'publish', 'slug',)

class CommentForm(forms.ModelForm):
    name = forms.CharField(required=True, widget=forms.TextInput(attrs={'placeholder': 'Your Name*'}))
    email = forms.EmailField(required=True, widget=forms.TextInput(attrs={'placeholder': 'Your Email*'}))
    website = forms.CharField(required=False, widget=forms.TextInput(attrs={'placeholder': 'Website'}))
    body = forms.CharField(required=True, widget=forms.Textarea(attrs={'placeholder': 'Your Comment*'}))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_show_labels = False

    class Meta:
        model = Comment
        fields = ('name', 'email', 'website', 'body')

"""
class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('name', 'email', 'website', 'body')
"""