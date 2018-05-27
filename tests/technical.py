"""
Ethiopian Transport API
Sample Test
"""

__author__ = "Dawit Nida (dawit@dawitnida.com)"
__date__ = "Date: 5-7-2018"
__version__ = "Version: "
__Copyright__ = "Copyright: @dawitnida"

from django.test import TestCase
from guzo.models import PriceQuota


class PriceQuotaTestCase(TestCase):
    def setUp(self):
        PriceQuota.objects.create(quota_code='DING', description='Ding dong!')

    def test_technical_has_system_lenght(self):
        """PriceQuota objects is correctly identified"""
        ding = PriceQuota.objects.get(quota_code='DING')
        self.assertEqual(ding.get_description(), 'Ding dong!')
