import factory

from mk_form.models import Data


class DataFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Data

    # Mocked Fields go here