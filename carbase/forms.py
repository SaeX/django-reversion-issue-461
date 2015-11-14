# -*- encoding: utf-8 -*-

from django import forms

from .models import CarMake, CarModel


class CarMakeCreateForm(forms.ModelForm):

    class Meta:
        model = CarMake
        fields = ('name', 'comments', )


class CarModelCreateForm(forms.ModelForm):

    class Meta:
        model = CarModel
        fields = ('make', 'model', 'comments', )
