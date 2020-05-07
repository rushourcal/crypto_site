from django import forms
from .models import UploadFile

class UploadFileForm(forms.Form):
    file = forms.FileField()
    isFile = False


class KeyInputForm(forms.Form):
    public = forms.CharField(widget=forms.Textarea)
    private = forms.CharField(widget=forms.Textarea)