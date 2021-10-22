import graphene
from graphene_django.types import DjangoObjectType
from api.graphql import ApiQuery


class Query(ApiQuery, graphene.ObjectType):
    check = graphene.Boolean()

    def resolve_check(self, info):
        print('info', info)
        return True


class Mutation(graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query)



