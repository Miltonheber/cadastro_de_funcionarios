from django.forms import ModelForm
from .models import Trabalhador


class TrabalhadorForm(ModelForm):
    class Meta:
        model = Trabalhador 
        fields = '__all__'

