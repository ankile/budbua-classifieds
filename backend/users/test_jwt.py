from django.test import TestCase

from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from .models import User


TEST_PASSWORD = "PUPASSWOrdLetsGO"
TEST_EMAIL = "bruker@budbua.no"

class Test_User(TestCase):
    def test_create_user(self):
        users_before = list(User.objects.values_list('id', flat=True).order_by('id'))
        test_user = User.objects.create( email='user@budbua.no', password='budbua')
        users_after = list(User.objects.values_list('id', flat=True).order_by('id'))

        self.assertNotEqual(users_after, users_before)

        test_user.delete()

        users_after = list(User.objects.values_list('id', flat=True).order_by('id'))
        self.assertEqual(users_after, users_before)



class Test_JWT_Authentication(TestCase):

   def test_produce_jwt_token(self):
        client = APIClient()
        jwt_auth_url = '/users/api-token-auth/'
        test_user = User(email=TEST_EMAIL)
        test_user.set_password(TEST_PASSWORD)

        test_user.is_active = False
        test_user.save()
        jwt_auth_response_fail = client.post(jwt_auth_url, {'email':'.no', 'password':'budbua'}, format='json')
        print(jwt_auth_response_fail)
        self.assertEqual(jwt_auth_response_fail.status_code, status.HTTP_400_BAD_REQUEST)

        test_user.is_active = True
        test_user.save()

        jwt_auth_response_success= client.post(jwt_auth_url, {'email':TEST_EMAIL, 'password':TEST_PASSWORD}, format='json')
        print(jwt_auth_response_success)
        self.assertEqual(jwt_auth_response_success.status_code, status.HTTP_200_OK)
        self.assertTrue('token' in jwt_auth_response_success.data)


   def test_verify_jwt_token(self):
       getTokenClient = APIClient()
       test_user = User(email=TEST_EMAIL)
       test_user.set_password(TEST_PASSWORD)
       test_user.save()
       jwt_auth_url = '/users/api-token-auth/'
       jwt_auth_get_token_response = getTokenClient.post(jwt_auth_url, {'email': TEST_EMAIL, 'password':TEST_PASSWORD}, format='json')
       token = jwt_auth_get_token_response.data['token']

       client = APIClient()
       get_users_url = '/users/'

       client.credentials(HTTP_AUTHORIZATION='JWT ' + 'abc')
       jwt_failed_authorization_response = client.get(get_users_url, date={'format': 'json'})
       self.assertEqual(jwt_failed_authorization_response.status_code, status.HTTP_401_UNAUTHORIZED)

       client.credentials(HTTP_AUTHORIZATION='JWT ' + token)
       jwt_successful_authorization_response = client.get(get_users_url, date={'format': 'json'})
       self.assertEqual(jwt_successful_authorization_response.status_code, status.HTTP_200_OK)




