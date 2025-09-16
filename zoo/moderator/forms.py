from django.forms import ModelForm, NumberInput, TextInput

from main.models import Animal


class Color:
    pass


class AnimalForm(ModelForm):
    class Meta:
        model = Animal
        fields = ["type", "color", "age", "zone"]
        widgets = {
            "type": TextInput(attrs={
                'class': "form-control",
                'placeholder': 'Вид'
            }),
            "color": TextInput(attrs={
                'class': "form-control",
                'placeholder': 'Колір'
            }),
            "age": NumberInput(attrs={
                'class': "form-control",
                'placeholder': 'Вік'
            }),
            "zone": NumberInput(attrs={
                'class': "form-control",
                'placeholder': 'Локація'
            })

        }

