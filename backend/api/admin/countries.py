from django.contrib.admin import register, ModelAdmin
from ..models import Countries


@register(Countries)
class CountriesAdminForm(ModelAdmin):
    list_display = ("name", "code", "population")
    list_display_links = ("name", "code", "population")
    search_fields = ("name",)
