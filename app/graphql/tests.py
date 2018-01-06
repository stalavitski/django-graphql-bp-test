from app.graphql.api import schema
from django_graphql_bp.user.tests import SchemaTestCase as UserSchemaTestCase
from graphene import Schema


class SchemaTestCase(UserSchemaTestCase):
    def get_schema(self) -> Schema:
        return schema