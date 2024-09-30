"""
URL configuration for mk project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path

from mk_form import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.HomeView.as_view(), name="home"),
    path("data_form", views.DataCreateView.as_view(), name="form"),
    path("data_list", views.DataListView.as_view(), name="data_list"),
    path("data_detail/<int:pk>", views.DataDetailView.as_view(), name="data_detail"),
    path("data_list/<int:pk>/edit", views.DataUpdateView.as_view(), name="data_edit"),
    path(
        "data_list/<int:pk>/delete",
        views.DataDeleteView.as_view(),
        name="data_delete",
    ),
]
