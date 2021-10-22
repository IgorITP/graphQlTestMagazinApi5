from api.models import Countries
from graphene_django.types import DjangoObjectType


class CountryNode(DjangoObjectType):
    class Meta:
        model = Countries

