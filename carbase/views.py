# -*- encoding: utf-8 -*-

from django.views import generic

from .models import CarMake, CarModel
from .forms import CarMakeCreateForm, CarModelCreateForm


class CarMakeCreateView(generic.CreateView):

    template_name = "carmake_add.html"
    form_class = CarMakeCreateForm


class CarMakeUpdateView(generic.UpdateView):

    template_name = "carmake_edit.html"
    form_class = CarMakeCreateForm
    model = CarMake


class CarMakeDetailView(generic.DetailView):
    
    template_name = "carmake_detail.html"
    model = CarMake


class CarModelCreateView(generic.CreateView):

    template_name = "carmodel_add.html"
    form_class = CarModelCreateForm


class CarModelUpdateView(generic.UpdateView):

    template_name = "carmodel_edit.html"
    form_class = CarModelCreateForm
    model = CarModel


class CarModelDetailView(generic.DetailView):
    
    template_name = "carmodel_detail.html"
    model = CarModel