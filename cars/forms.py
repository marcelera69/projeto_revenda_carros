from typing import Any
from django import forms
from cars.models import Car
import datetime


class CarForm(forms.ModelForm):

    class Meta():
        model = Car
        fields = '__all__'

    def clean_model(self):
        model = str(self.cleaned_data.get('model'))
        model = model.capitalize().strip()
        return model


    def clean_value(self):
        value = self.cleaned_data.get('value')

        if value < 0:
            self.add_error('value', 'O valor do Automóvel tem que ser maior que R$0')
        
        return value
    

    def clean_factory_year(self):
        factory_year = self.cleaned_data.get('factory_year')

        if factory_year == None:
            return factory_year

        if factory_year > datetime.datetime.now().year:
            self.add_error('factory_year', f'O ano de fabricação não pode ser maior que {datetime.datetime.now().year}')

        return factory_year
    

    def clean_model_year(self):
        model_year = self.cleaned_data.get('model_year')

        if model_year < 1975:
            self.add_error('model_year', 'O modelo do carro é muito antigo para a nossa loja (acima de 1975)')

        return model_year
    

    def clean_km(self):
        km = self.cleaned_data.get('km')

        if km < 0:
            self.add_error('km', 'A quilometragem do automóvel não pode ser menor que 0KM')
        
        return km
    