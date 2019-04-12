from django.contrib.auth.models import Group
from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient

from users.models import User

TEST_PASSWORD = "PUPASSWOrdLetsGO"
TEST_EMAIL = "bruker@budbua.no"


class Test_User_View(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.getTokenClient = APIClient()
        cls.test_user = User(email=TEST_EMAIL)
        cls.test_user.set_password(TEST_PASSWORD)
        cls.test_user.save()
        jwt_auth_url = '/users/api-token-auth/'
        cls.jwt_auth_get_token_response = cls.getTokenClient.post(jwt_auth_url,
                                                                  {'email': TEST_EMAIL, 'password': TEST_PASSWORD},
                                                                  format='json')
        cls.token = cls.jwt_auth_get_token_response.data['token']

        cls.getTokenClient.credentials(HTTP_AUTHORIZATION='JWT ' + cls.token)

        cls.analytics_url = '/analytics/'
        cls.ownerGroup = Group.objects.get(name='Owner')

    def test_get_analytics_via_rest_fail(self):
        create_user_response_fail = self.getTokenClient.get(self.analytics_url)
        self.assertEqual(create_user_response_fail.status_code, status.HTTP_403_FORBIDDEN)

    def test_get_analytics_via_rest_success(self):
        self.ownerGroup.user_set.add(self.test_user)
        create_user_response_success = self.getTokenClient.get(self.analytics_url)
        self.assertEqual(create_user_response_success.status_code, status.HTTP_200_OK)
