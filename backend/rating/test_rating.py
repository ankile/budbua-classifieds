from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient

from users.models import User

TEST_PASSWORD = "PUPASSWOrdLetsGO"
TEST_EMAIL = "bruker@budbua.no"


class Test_Report_View(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.getTokenClient = APIClient()
        test_user = User(email=TEST_EMAIL)
        test_user.set_password(TEST_PASSWORD)
        test_user.save()
        jwt_auth_url = '/users/api-token-auth/'
        cls.jwt_auth_get_token_response = cls.getTokenClient.post(jwt_auth_url,
                                                                  {'email': TEST_EMAIL, 'password': TEST_PASSWORD},
                                                                  format='json')
        cls.token = cls.jwt_auth_get_token_response.data['token']

        cls.getTokenClient.credentials(HTTP_AUTHORIZATION='JWT ' + cls.token)

        cls.bad_get_user_rating = '/rating/?ratingReceiver=38'
        cls.good_get_user_rating = '/rating/?ratingReceiver=2'

        cls.bad_put_user_rating = '/rating/?ratingReceiver=38'
        cls.good_put_user_rating = '/rating/?ratingReceiver=2'

        cls.bad_post_user_rating = '/rating/?ratingReceiver=38'
        cls.good_post_user_rating = '/rating/?ratingReceiver=2'

        cls.test_user_reported = User.objects.create(email='user@budbua.no', password='budbua')

    def test_post_user_rating_via_rest(self):
        inserting_failed_user_rating = self.getTokenClient.post(self.bad_post_user_rating, {'rating': 4}, format='json')
        self.assertEqual(inserting_failed_user_rating.status_code, status.HTTP_400_BAD_REQUEST)

        inserting_success_user_rating = self.getTokenClient.post(self.good_post_user_rating, {'rating': 4},
                                                                 format='json')
        self.assertEqual(inserting_success_user_rating.status_code, status.HTTP_201_CREATED)

    def test_put_user_rating_via_rest(self):
        inserting_failed_user_rating = self.getTokenClient.post(self.bad_post_user_rating, {'rating': 4}, format='json')
        self.assertEqual(inserting_failed_user_rating.status_code, status.HTTP_400_BAD_REQUEST)

        inserting_success_user_rating = self.getTokenClient.post(self.good_post_user_rating, {'rating': 4},
                                                                 format='json')
        self.assertEqual(inserting_success_user_rating.status_code, status.HTTP_201_CREATED)

        inserting_success_put_user_rating = self.getTokenClient.put(self.good_put_user_rating, {'rating': 3},
                                                                    format='json')
        self.assertEqual(inserting_success_put_user_rating.status_code, status.HTTP_200_OK)

    def test_put_user_rating_via_rest(self):
        inserting_failed_user_rating = self.getTokenClient.post(self.bad_post_user_rating, {'rating': 4}, format='json')
        self.assertEqual(inserting_failed_user_rating.status_code, status.HTTP_400_BAD_REQUEST)

        inserting_success_user_rating = self.getTokenClient.post(self.good_post_user_rating, {'rating': 4},
                                                                 format='json')
        self.assertEqual(inserting_success_user_rating.status_code, status.HTTP_201_CREATED)

        inserting_failed_get_user_rating = self.getTokenClient.get(self.bad_get_user_rating)
        self.assertEqual(inserting_failed_get_user_rating.status_code, status.HTTP_204_NO_CONTENT)

        inserting_success_get_user_rating = self.getTokenClient.get(self.good_get_user_rating)
        self.assertEqual(inserting_success_get_user_rating.status_code, status.HTTP_200_OK)
