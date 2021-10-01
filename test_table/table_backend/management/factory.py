from table_backend.models import Table
import factory
from faker import Faker
from random import randint

class TableFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Table

    date = factory.Faker('date_time')
    name = factory.Faker('name')
    amount = factory.Faker('pyint', min_value=1, max_value=100)
    distance = factory.Faker('pyint', min_value=1, max_value=10000)





