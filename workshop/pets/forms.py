from django import forms
from workshop.pets.models import Pet


class PetBaseForm(forms.ModelForm):
    class Meta:
        model = Pet
        fields = ['name', 'date_of_birth', 'personal_photo']
        widgets = {
            'name': forms.TextInput(
                attrs={
                    'placeholder': 'Pet name'
                }
            ),
            'date_of_birth': forms.DateInput(
                attrs={
                    'type': 'date'
                }
            ),
            'personal_photo': forms.TextInput(
                attrs={
                    'placeholder': 'Link to image'
                }
            ),
        }
        labels = {
            'name': 'Pet Name',
            'date_of_birth': 'Date of Birth',
            'personal_photo': 'Link to Image'
        }


class PetCreateForm(PetBaseForm):
    pass


class PetEditForm(PetBaseForm):
    pass


class PetDeleteForm(PetBaseForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__disable_fields()

    def __disable_fields(self):
        for name, field in self.fields.items():
            field.widget.attrs['disabled'] = 'disabled'
            field.widget.attrs['readonly'] = 'readonly'
