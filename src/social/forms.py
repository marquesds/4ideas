from django.forms import ModelForm
from .models import Post


class PostForm(ModelForm):
    def __init__(self, player=None, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)
        self.player = player

    def save(self, commit=True):
        post = super(PostForm, self).save(commit=False)
        post.player = self.player
        if commit:
            post.save()
        return post

    class Meta:
        model = Post
        fields = ['content']
