from django.contrib.auth.models import User
from .models import *
from django import forms


class CommentForm(forms.ModelForm):
    rating = forms.ChoiceField(initial=0,
                               choices=((1, 1), (2, 2), (3, 3), (4, 4), (5, 5)), help_text="Rating:", required=True)
    content = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control'}), max_length=Comment.COMMENT_MAX_LENGTH,
                             help_text="Please type your comments:", required=True)

    class Meta:
        model = Comment
        fields = ('rating', 'content')

