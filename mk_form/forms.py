from django import forms

from mk_form.models import Data


class DataForm(forms.ModelForm):
    class Meta:
        model = Data
        fields = "__all__"
