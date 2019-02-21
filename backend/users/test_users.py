from django.test import TestCase

from rest_framework.test import APIClient
from rest_framework import status
from .models import User

TEST_PASSWORD = "PUPASSWOrdLetsGO"
TEST_EMAIL = "bruker@budbua.no"



class Test_User_View(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.getTokenClient = APIClient()
        test_user = User(email=TEST_EMAIL)
        test_user.set_password(TEST_PASSWORD)
        test_user.save()
        jwt_auth_url = '/users/api-token-auth/'
        cls.jwt_auth_get_token_response = cls.getTokenClient.post(jwt_auth_url, {'email': TEST_EMAIL, 'password':TEST_PASSWORD}, format='json')
        cls.token = cls.jwt_auth_get_token_response.data['token']

        cls.getTokenClient.credentials(HTTP_AUTHORIZATION='JWT ' + cls.token)

        cls.user_url = '/users/'

    def test_user_register_via_rest(self):
        pass

    def test_user_login_via_rest(self):
        pass

