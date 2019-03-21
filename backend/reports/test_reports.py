from django.test import TestCase

from rest_framework.test import APIClient
from rest_framework import status
from users.models import User
from auctions.models import Ad
from budbua.utils.dateutils import today
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
        cls.jwt_auth_get_token_response = cls.getTokenClient.post(jwt_auth_url, {'email': TEST_EMAIL, 'password':TEST_PASSWORD}, format='json')
        cls.token = cls.jwt_auth_get_token_response.data['token']

        cls.getTokenClient.credentials(HTTP_AUTHORIZATION='JWT ' + cls.token)

        cls.bad_user_report_url= '/reports/users/99/'
        cls.good_user_report_url= '/reports/users/2/'


        cls.bad_ad_report_url= '/reports/ads/99/'
        cls.good_ad_report_url= '/reports/ads/1/'

        cls.test_user_reported = User.objects.create(email='user@budbua.no', password='budbua')

        cls.ad = Ad.objects.create(owner=cls.test_user_reported, title='testAD', description='the best ad ever', bid_end_time=today(cls))

    def test_report_user_via_rest(self):

        inserting_failed_report = self.getTokenClient.post(self.bad_user_report_url)
        self.assertEqual(inserting_failed_report.status_code, status.HTTP_400_BAD_REQUEST)

        inserting_successful_report= self.getTokenClient.post(self.good_user_report_url)
        self.assertEqual(inserting_successful_report.status_code, status.HTTP_201_CREATED)


    def test_report_ad_via_rest(self):

        inserting_failed_report = self.getTokenClient.post(self.bad_ad_report_url)
        self.assertEqual(inserting_failed_report.status_code, status.HTTP_400_BAD_REQUEST)

        inserting_successful_report= self.getTokenClient.post(self.good_ad_report_url)
        self.assertEqual(inserting_successful_report.status_code, status.HTTP_201_CREATED)


