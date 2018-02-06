from app.graphql.api import schema
from django_graphql_bp.user.tests import *
from graphene import Schema


class GraphqlTestCase(cases.OperationTestCase):
    def get_schema(self) -> Schema:
        return schema

    def setUp(self):
        super(GraphqlTestCase, self).setUp()

    def set_up_user(self):
        self.user = self.create_test_user('user', {'username': 'user'})
        self.user2 = self.create_test_user('user2', {'username': 'user2'})
        self.staff = self.create_test_user('staff', {'username': 'staff'})
        self.staff.is_staff = True
        self.staff.save()