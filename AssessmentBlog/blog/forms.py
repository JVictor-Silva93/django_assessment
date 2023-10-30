from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment #Ensure that this form is associated with the Comment model
        fields = '__all__'  

