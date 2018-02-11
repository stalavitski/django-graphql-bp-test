import graphene
import django_graphql_bp.article.schema
import django_graphql_bp.user.schema


class Queries(
    django_graphql_bp.article.schema.Query,
    django_graphql_bp.user.schema.Query,
    graphene.ObjectType
):
    pass


class Mutations(
    django_graphql_bp.article.schema.Mutation,
    django_graphql_bp.user.schema.Mutation,
    graphene.ObjectType
):
    pass


schema = graphene.Schema(query=Queries, mutation=Mutations)
