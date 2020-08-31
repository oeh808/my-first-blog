from django import forms
from .models import Post
from .models import cvText
from .models import cvList

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text',)

class PostCvText(forms.ModelForm):

    class Meta:
        model = cvText
        fields = ('text',)

class PostCvList(forms.ModelForm):

    class Meta:
        model = cvList
        fields = ('text',)
