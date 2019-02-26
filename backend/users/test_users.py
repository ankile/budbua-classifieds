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
        cls.test_user = User(email=TEST_EMAIL)
        cls.test_user.set_password(TEST_PASSWORD)
        cls.test_user.save()
        jwt_auth_url = '/users/api-token-auth/'
        cls.jwt_auth_get_token_response = cls.getTokenClient.post(jwt_auth_url, {'email': TEST_EMAIL, 'password':TEST_PASSWORD}, format='json')
        cls.token = cls.jwt_auth_get_token_response.data['token']

        cls.getTokenClient.credentials(HTTP_AUTHORIZATION='JWT ' + cls.token)

        cls.user_url = '/users/'


    def test_user_register_via_rest(self):
        client = APIClient()
        registerUserData = {
            "email": "scammerMacScammy@budbua.no",
            "password": "iamnotascammer",
            "password2": "iamnotascammer"
        }

        create_user_url = '/users/create/'

        create_user_response_fail = client.post(create_user_url, {"firstname": "yo"}, format='json')
        self.assertEqual(create_user_response_fail.status_code, status.HTTP_400_BAD_REQUEST)

        create_user_response_success = client.post(create_user_url, registerUserData, format='json')
        self.assertEqual(create_user_response_success.status_code, status.HTTP_201_CREATED)


    def test_user_register_via_rest_wrong_second_password(self):
        client = APIClient()
        registerUserData = {
            "email": "scammerMacScammy@budbua.no",
            "password": "iamnotascammer",
            "password2": "iAMascammer"
        }

        create_user_url = '/users/create/'

        create_user_response_fail = client.post(create_user_url, registerUserData, format='json')
        self.assertEqual(create_user_response_fail.status_code, status.HTTP_400_BAD_REQUEST)

    def test_user_get_profile(self):

        get_profile_response = self.getTokenClient.get(self.user_url)
        self.assertEqual(get_profile_response.status_code, status.HTTP_200_OK)

    def test_user_get_profile_content(self):
        expectedDataFail = {
            "id": 1,
            "first_name": "Kent",
            "last_name": "Torvik",
            "email": "bruker@budbua.no"
        }
        get_profile_response = self.getTokenClient.get(self.user_url)

        self.assertNotEqual(get_profile_response.data, expectedDataFail)

        expectedDataSuccess = {
            "id": 1,
            "first_name": None,
            "last_name": None,
            "email": "bruker@budbua.no"
        }

        self.assertEqual(get_profile_response.data, expectedDataSuccess)

    def test_user_get_profile_expected_fields(self):
        get_profile_response = self.getTokenClient.get(self.user_url)

        self.assertNotIn('scammer', get_profile_response.data.keys())

        self.assertIn('id', get_profile_response.data.keys())
        self.assertIn('first_name', get_profile_response.data.keys())
        self.assertIn('last_name', get_profile_response.data.keys())
        self.assertIn('email', get_profile_response.data.keys())


    def test_user_profile_update(self):
        updateDate = {
            "firstName": "Kent Are",
            "lastName": "Torvik",
            "email": TEST_EMAIL,
            "password": TEST_PASSWORD,
            "password2": TEST_PASSWORD
        }
        client = APIClient()

        put_profile_update_response_fail = client.put(self.user_url, updateDate, format='json')
        self.assertEqual(put_profile_update_response_fail.status_code, status.HTTP_401_UNAUTHORIZED)

        put_profile_update_response_success = self.getTokenClient.put(self.user_url, updateDate, format='json')
        self.assertEqual(put_profile_update_response_success.status_code, status.HTTP_200_OK)


    def test_user_profile_update_wrong_password(self):
        updateDate = {
            "firstName": "Kent Are",
            "lastName": "Torvik",
            "email": TEST_EMAIL,
            "password": TEST_PASSWORD,
            "password2": "WRONG PASSSORD"
        }

        put_profile_update_response_wrong_password = self.getTokenClient.put(self.user_url, updateDate, format='json')
        self.assertEqual(put_profile_update_response_wrong_password.status_code, status.HTTP_400_BAD_REQUEST)

    def test_user_delete_own_profile(self):
         client = APIClient()
         test_user = User(email="budbuaTest@budbua.no")
         test_user.set_password('pleaseDoNOTdeleteM3')
         test_user.save()
         jwt_auth_url = '/users/api-token-auth/'
         jwt_auth_get_token_response = client.post(jwt_auth_url, {'email': "budbuaTest@budbua.no", 'password':"pleaseDoNOTdeleteM3"}, format='json')
         token = jwt_auth_get_token_response.data['token']
         client.credentials(HTTP_AUTHORIZATION='JWT ' + token)

         delete_profile_response = client.delete(self.user_url)
         self.assertEqual(delete_profile_response.status_code, status.HTTP_204_NO_CONTENT)



    def test_user_delete_own_profile_fail(self):
        client = APIClient()
        test_user = User(email="budbuaTest@budbua.no")
        test_user.set_password('pleaseDoNOTdeleteM3')
        test_user.save()
        jwt_auth_url = '/users/api-token-auth/'
        jwt_auth_get_token_response = client.post(jwt_auth_url, {'email': "budbuaTest@budbua.no", 'password':"pleaseDoNOTdeleteM3"}, format='json')

        delete_profile_response = client.delete(self.user_url)
        self.assertEqual(delete_profile_response.status_code, status.HTTP_401_UNAUTHORIZED)





