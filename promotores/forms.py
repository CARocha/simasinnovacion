# -*- coding: utf-8 -*-

from django import forms
from .models import *

YEAR_ACTIVO = (
                                (1, '2009'),
                                (2, '2010'),
                                (3, '2011'),
                                (4, '2012'),
                                (5, '2013'),
                                (6, '2014'),
                                (7, '2015'),
                                (8, '2016'),
                            )

class PromotorForm(forms.Form):
    zona = forms.ChoiceField(choices=[('', 'zona'),(1, 'Seca'),(2, 'Alta'),
                            (3, 'Húmeda')],required=False)
    organizacion_civil = forms.ModelMultipleChoiceField(queryset=OrganizacionCivil.objects.all().order_by('nombre'),
                            required=False)
    sexo = forms.ChoiceField(choices=[('', 'sexo'),(1,'Masculino'),
                                      (2, 'Femenino')],
                                      required=False)
    activo = forms.MultipleChoiceField(choices=YEAR_ACTIVO, required=False)

def get_anios():
    years = []
    for en in PracticasProductivas.objects.order_by('anio').values_list('anio', flat=True):
        years.append((en, en))
    return list(set(years))

class CustomChoiceField(forms.ChoiceField):
    def __init__(self, *args, **kwargs):
        super(CustomChoiceField, self).__init__(*args, **kwargs)
        self.choices.insert(0, ('', 'Año'))

class PracticaForm(forms.Form):
    zona = forms.ChoiceField(choices=[('', 'zona'),(1, 'Seca'),(2, 'Alta'),
                            (3, 'Húmeda')],required=False)
    anio = CustomChoiceField(choices=get_anios())
    tema_prueba = forms.ModelChoiceField(queryset=TemasPruebas.objects.all().order_by('nombre'),
                            required=False, empty_label="Tema")
    rubro_prueba = forms.ModelChoiceField(queryset=RubroPruebas.objects.all().order_by('nombre'),
                            required=False, empty_label="Rubro")
    escala_prueba = forms.ModelChoiceField(queryset=EscalaPruebas.objects.all().order_by('nombre'),
                            required=False, empty_label="Escala")
