from django.test import TestCase

from rest_framework.test import APIClient
from rest_framework import status
from .models import User, Ad
import datetime
from datetime import timedelta


TEST_PASSWORD = "PUPASSWOrdLetsGO"
TEST_EMAIL = "bruker@budbua.no"


class Test_Ads_View(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.authorizedClient = APIClient()
        cls.test_user = User(email=TEST_EMAIL)
        cls.test_user.set_password(TEST_PASSWORD)
        cls.test_user.save()
        jwt_auth_url = '/users/api-token-auth/'
        cls.jwt_auth_get_token_response_test_user = cls.authorizedClient.post(jwt_auth_url, {'email': TEST_EMAIL, 'password':TEST_PASSWORD}, format='json')
        cls.token = cls.jwt_auth_get_token_response_test_user.data['token']

        cls.authorizedClient.credentials(HTTP_AUTHORIZATION='JWT ' + cls.token)

        cls.unauthorizedClient = APIClient()
        cls.test_user_unauth = User(email='kent@notallowedtodelete.no')
        cls.test_user_unauth.set_password(TEST_PASSWORD)
        cls.test_user_unauth.save()
        cls.jwt_auth_get_token_response_test_user_unauth = cls.unauthorizedClient.post(jwt_auth_url, {'email': 'kent@notallowedtodelete.no', 'password':TEST_PASSWORD}, format='json')
        cls.token_unauth = cls.jwt_auth_get_token_response_test_user_unauth.data['token']

        cls.unauthorizedClient.credentials(HTTP_AUTHORIZATION='JWT ' + cls.token_unauth)


        cls.test_time_now = datetime.datetime.now().isoformat()


    def setUp(self):
        # Set up two ads
        self.ad1 = Ad(
            owner=self.test_user,
            title = "Fotball",
            description = "Fotball selges",
            bid_end_time = self.test_time_now,
            minimum_bid =  3,
            zip_code = 7034 )
        self.ad1.save()
        self.ad2 = Ad(
            owner=self.test_user,
            title = "Handball",
            description = "Handball selges",
            bid_end_time = self.test_time_now,
            minimum_bid =  99,
            zip_code = 7009 )
        self.ad2.save()


        pass

    def test_ads_create(self):
        # Post
        # CREATED 201 on success
        # {
        #     "title": string,
        #     "description": string,
        #     "bidEndTime": "YYYY-MM-DDTHH:MM",
        #     "minimumBid": int, (default=0)
        #     "zipCode": int(optional)
        # }

        ads_create_url = '/auctions/ads/'
        client = APIClient()

        #fail
        failData = {
            "title": "Fotball",
            "bidEndTime": self.test_time_now,
            "minimumBid": 3,
            "zipCode": 7034
        }

        unauthorized_response = client.post(ads_create_url, failData, format='json')
        self.assertEqual(unauthorized_response.status_code, status.HTTP_401_UNAUTHORIZED)

        bad_request_response = self.authorizedClient.post(ads_create_url, failData, format='json')
        self.assertEqual(bad_request_response.status_code, status.HTTP_400_BAD_REQUEST)

        #success
        successData = {
            "title": "Fotball",
            "description": "Fotball selges",
            "bidEndTime": self.test_time_now,
            "minimumBid": 3,
            "zipCode": 7034
        }

        success_request_response = self.authorizedClient.post(ads_create_url, successData, format='json')
        self.assertEqual(success_request_response.status_code, status.HTTP_201_CREATED)

    def test_ads_delete_other_users_ads(self):
        #DELETE - /auctions/ads/<int:pk>/
        #NO CONTENT 204
        ads_delete_url = '/auctions/ads/1/'

        #unauthorized, delete others ads
        unauthorized_response = self.unauthorizedClient.delete(ads_delete_url)
        self.assertEqual(unauthorized_response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_ads_delete(self):
        #DELETE - /auctions/ads/<int:pk>/
        #NO CONTENT 204
        ads_delete_url_fail = '/auctions/ads/44/'
        ads_delete_url_success = '/auctions/ads/1/'

        #fail - ad doesn't exist
        failed_response = self.authorizedClient.delete(ads_delete_url_fail)
        self.assertEqual(failed_response.status_code, status.HTTP_400_BAD_REQUEST)



        #success

        success_response = self.authorizedClient.delete(ads_delete_url_success)
        self.assertEqual(success_response.status_code, status.HTTP_204_NO_CONTENT)
        pass


    def test_ads_detail_view_when_clicked(self):
        #GET - /auctions/ads/<int:pk>/ get a specific ad
        # Returns OK 200
        # {
        #     "id": int,
        #     "owner": int,
        #     "title": string,
        #     "description": string,
        #     "image": base64, (not implemented)
        #     "minimumBid": int,
        #     "bidEndTime": date,
        #     "rating": 'int', (not implemented)
        #     "zipCode": int,
        #     "firstName": string,
        #     "lastName": string,
        #     "email": string,
        #     "highestBidder": {
        #           "id": int,
        #           "name": string
        #       },
        # }
        ads_test_ads_detail_url = '/auctions/ads/1/'
        pass

    def test_ads_detail_view_when_clicked_keys(self):
        ads_test_ads_detail_url = '/auctions/ads/1/'
        pass


    def test_ads_list_frontpage(self):
        # GET - /auctions/ads/?search=<search query> get a list of ads
        # [
        #     {
        #         "id": int,
        #         "title": string,
        #         "description": string,
        #         "image": base64, (not implemented)
        #         "minimumBid": int,
        #         "bidEndTime": date
        #      },
        #   {
        #     ...
        #   }
        # ]


        pass

