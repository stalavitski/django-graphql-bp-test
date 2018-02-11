from django_graphql_bp.user.tests import *
from django_graphql_bp.article.tests import *


class GraphqlTestCase(cases.OperationTestCase):
    def setUp(self):
        super(GraphqlTestCase, self).setUp()

    def set_up_user(self):
        self.user = self.create_test_user('user', {'username': 'user'})
        self.user2 = self.create_test_user('user2', {'username': 'user2'})
        self.staff = self.create_test_user('staff', {'username': 'staff'})
        self.staff.is_staff = True
        self.staff.save()
