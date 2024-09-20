from datetime import datetime
from django.views.generic import TemplateView


class HomeView(TemplateView):
    template_name = "mk_form/home.html"
    extra_context = {"today": datetime.today()}
