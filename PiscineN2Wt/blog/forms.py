from django import forms
from .models import MonPost
    
class CommentModelForm(forms.ModelForm):
    class Meta:
        model = MonPost
        fields = ['title', 'content', 'author']