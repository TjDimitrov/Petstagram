from django import forms

from workshop.photos.models import Photo


class PhotoBaseForm(forms.ModelForm):
    fields = '__all__'
    class Meta:
        model = Photo
        exclude = ['date_of_publication']


class PhotoCreateForm(PhotoBaseForm):
    class Meta:
        model = Photo
        fields = '__all__'
        exclude = ['user']


class PhotoEditForm(PhotoBaseForm):
    class Meta:
        model = Photo
        exclude = ['photo']


class PhotoDeleteForm(PhotoBaseForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for name, field in self.fields.items():
            field.widget.attrs['disabled'] = 'disabled'
            field.widget.attrs['readonly'] = 'readonly'

