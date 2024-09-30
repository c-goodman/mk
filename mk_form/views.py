from datetime import datetime
from django.views.generic import TemplateView
from django.views.generic import CreateView, DetailView, ListView, UpdateView
from django.views.generic.edit import DeleteView

from mk_form.models import Data
from mk_form.forms import DataModelForm


class HomeView(TemplateView):
    template_name = "mk_form/home.html"
    extra_context = {"today": datetime.today()}


class DataCreateView(CreateView):
    model = Data
    success_url = "/"
    form_class = DataModelForm
    template_name = "mk_form/data_form.html"
