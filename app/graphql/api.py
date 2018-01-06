import graphene
from django_graphql_bp.graphql.api import UserQueries, UserMutations


class Queries(UserQueries):
    pass


class Mutations(UserMutations):
    pass


schema = graphene.Schema(query=Queries, mutation=Mutations)
