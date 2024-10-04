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
    success_url = "/data_list"
    form_class = DataModelForm
    template_name = "mk_form/data_form.html"
    extra_context = {"today": datetime.today()}


class DataListView(ListView):
    model = Data
    success_url = "data_forms"
    template_name = "mk_form/data_list.html"


class DataDetailView(DetailView):
    model = Data
    context_object_name = "data_form"


class DataUpdateView(UpdateView):
    model = Data
    success_url = "/data_list"
    form_class = DataModelForm
    extra_content = {"today": datetime.today()}


class DataDeleteView(DeleteView):
    model = Data
    success_url = "/data_list"
    template_name = "mk_form/data_delete.html"
    context_object_name = "data_form"
