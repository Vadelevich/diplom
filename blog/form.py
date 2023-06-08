from django import forms

from blog.models import Comment


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = '__all__'


    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        for name,field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'