from graphene import ObjectType, List, Field
from api.models import Countries
from .country_node import CountryNode


class GetListCountries(ObjectType):
    get_list_countries = Field(lambda: List(CountryNode))

    def resolve_get_list_countries(self, info):
        return Countries.objects.all()
