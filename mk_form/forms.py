from django import forms

from mk_form.models import Data

# TODO: Use forms.Form instead, no 'fields = "__all__"'
class DataModelForm(forms.ModelForm):
    class Meta:
        model = Data
        fields = "__all__"


class DataForm(forms.Form):
    pass
