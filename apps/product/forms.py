from django import forms
from .models import Review
class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        field = '__all__'
        exclude = ['product', 'author']

        def __init__(self, *args, **kwargs):
            super(ReviewForm, self).__init__(*args, **kwargs)
            for field_name, field in self.fields.items():
                field.widget.attrs['class'] = 'bor8 stext-102 cl2 p-lr-20'
                field.widget.attrs['placeholder'] = field_name.capitalize()