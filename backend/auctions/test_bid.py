from django.test import TestCase

from rest_framework.test import APIClient
from rest_framework import status
from users.models import User
from auctions.models import Ad, Bid
from budbua.utils.dateutils import today
from django.core.exceptions import ValidationError
from .serializers import BidSerializer


TEST_PASSWORD = "PUPASSWOrdLetsGO"
TEST_EMAIL = "bruker@budbua.no"

class Test_Bid_Model(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.test_user_ad_owner = User.objects.create(email='user@budbua.no', password='budbua')
        cls.test_user_ad_bidder = User.objects.create(email='bidder@bidder.no', password='budbua')
        cls.ad = Ad.objects.create(owner=cls.test_user_ad_owner, title='testAD', description='the best ad ever', bid_end_time=today(cls))
        cls.bid = Bid.objects.create(bidder=cls.test_user_ad_bidder, ad=cls.ad, value=1000)

    def test_bid_bidder_label(self):
        bid = Bid.objects.get(id=1)
        field_label = bid._meta.get_field('bidder').verbose_name
        self.assertEquals(field_label, 'bidder')

    def test_bid_ad_label(self):
        bid = Bid.objects.get(id=1)
        field_label = bid._meta.get_field('ad').verbose_name
        self.assertEquals(field_label, 'ad')

    def test_bid_value_label(self):
        bid = Bid.objects.get(id=1)
        field_label = bid._meta.get_field('value').verbose_name
        self.assertEquals(field_label, 'value')

    def test_bid_owner_cant_bid_on_own_ad(self):
        with self.assertRaises(ValidationError):
            Bid.objects.create(bidder=self.test_user_ad_owner, ad=self.ad, value=3000)

class Test_Bid_Serializer:
    @classmethod
    def setUp(self):
        self.bid_attributes = {
            'bidder': 1,
            'ad': 1,
            'value': 3000
        }

        self.serializer_data = {
            'bidder': 5,
            'ad': 2,
            'value': 3000
        }

        self.test_user_ad_owner = User.objects.create(email='user@budbua.no', password='budbua')
        self.test_user_ad_bidder = User.objects.create(email='bidder@bidder.no', password='budbua')
        self.ad = Ad.objects.create(owner=self.test_user_ad_owner, title='testAD', description='the best ad ever', bid_end_time=today(cls))

        self.bid = Bid.objects.create(**self.bid_attributes)
        self.serializer = BidSerializer(instance=self.bid)

    def test_bid_contains_expected_fields(self):
        data = self.serializer.data
        self.assertItemsEqual(set(data.keys()), ['bidder', 'ad', 'value'])

    def test_bidder_field_content(self):
        data = self.serializer.data
        self.assertEqual(data['bidder'], self.bid_attributes['bidder'])

    def test_ad_field_content(self):
        data = self.serializer.data
        self.assertEqual(data['ad'], self.bid_attributes['ad'])

    def test_value_field_content(self):
        data = self.serializer.data
        self.assertEqual(data['value'], self.bid_attributes['value'])

class Test_Bid_View(TestCase):
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

        cls.bad_add_bid_url = '/auctions/ads/99/bid/'
        cls.good_add_bid_url = '/auctions/ads/1/bid/'


        cls.test_user_ad_owner = User.objects.create(email='user@budbua.no', password='budbua')
        cls.ad = Ad.objects.create(owner=cls.test_user_ad_owner, title='testAD', description='the best ad ever', bid_end_time=today(cls))

    def test_bid_inserting_via_rest(self):

        inserting_failed_bid = self.getTokenClient.post(self.bad_add_bid_url,{'value':3000}, format='json')
        self.assertEqual(inserting_failed_bid.status_code, status.HTTP_400_BAD_REQUEST)

        inserting_successful_bid = self.getTokenClient.post(self.good_add_bid_url,{'value':3000}, format='json')
        self.assertEqual(inserting_successful_bid.status_code, status.HTTP_201_CREATED)




