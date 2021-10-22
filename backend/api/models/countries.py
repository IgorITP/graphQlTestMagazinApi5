from django.db.models import CharField, Model


class Countries(Model):
    name = CharField(verbose_name='Name', default="", max_length=100, blank=False)
    code = CharField(verbose_name='Code', default="", max_length=100, blank=False)
    population = CharField(verbose_name='Population', default="", max_length=100, blank=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Country"
        verbose_name = "Countries"
