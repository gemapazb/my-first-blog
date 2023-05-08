from django import froms
from .models import Post

class Postform(forms.Modelform):
    class Meta:
        model = Post
        fields = ('title', 'text',)
    

