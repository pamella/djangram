from django import forms

from posts.models import Post

# Django Model form
# https://docs.djangoproject.com/pt-br/2.2/topics/forms/modelforms/

class PostCreateForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['author', 'image', 'description', ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['author'].initial = self.initial['user'].id
        self.fields['author'].widget = forms.HiddenInput()


