from django import forms


class BlogCreateForm(forms.Form):
    title = forms.CharField()
    body = forms.CharField(widget=forms.Textarea(attrs={'rows': 4}))
    created = forms.DateTimeField()
