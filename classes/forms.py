from django import forms
from .models import Class_Type, Level, Ratings


class ClassTypeForm(forms.ModelForm):

    class Meta:
        model = Class_Type
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        level = Level.objects.all()
        friendly_names = [(l.id, l.get_friendly_name()) for l in level]

        self.fields['level'].choices = friendly_names
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'rounded-0'


class RatingsForm(forms.ModelForm):
    class Meta:
        model = Ratings
        fields = ('author', 'class_name', 'rating', 'review',)

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'author': 'Author',
            'class_name': 'Class Name',
            'rating': 'Rating',
            'review': 'Review',
            'date': 'Date',
        }

        self.fields['author'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if self.fields[field].required:
                placeholder = f'{placeholders[field]} *'
            else:
                placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].label = False
