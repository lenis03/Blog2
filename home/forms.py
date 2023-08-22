from django import forms

from .models import Blog


class BlogCreateForm(forms.Form):
    title = forms.CharField()
    body = forms.CharField(widget=forms.Textarea(attrs={'rows': 4}))
    created = forms.DateTimeField()


class BlogUpdateForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = '__all__'
