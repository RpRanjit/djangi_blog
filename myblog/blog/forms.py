from django import forms
from .models import Comment, Blog

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = {'name', 'email', 'body'}

        widgets= {
            'name': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control'
            }),
            'body': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3
            })
        }

class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ('title', 'image', 'category', 'description', 'content')

        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                
            }),
            'image': forms.URLInput(attrs={
                'class': 'form-control',
                'placeholder': 'https://example.com/image.jpg'
            }),
            'category': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3,
                'placeholder': 'Write a short description'
            }),
            'content': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 12,
                'placeholder': 'Write your amazing content here...'
            })
        }
        
        