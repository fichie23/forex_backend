import json

from faker import Faker
from django.test import TestCase
from models import ExchangeRateHistory


# Create your tests here.
class ForexViewTest(TestCase):

    def setUp(self):
        self.fake = Faker()
        self.base = self.fake.currency_code()
        self.target = self.fake.currency_code()

    def test_submit_daily_exchange_rate(self):
        data = {
            "currency": {
                "base": self.base,
                "target": self.target
            },
            "date": self.fake.date(pattern="%Y-%m-%d", end_datetime=None),
            "rate": self.fake.pyfloat(left_digits=1, right_digits=3, positive=True)
        }
        response = self.client.post('/forex/exchange/', json.dumps(data), content_type="application/json")
        self.assertEqual(response.status_code, 201)

    def test_list_daily_exchange_rate(self):
        data = {
            "currency": {
                "base": self.base,
                "target": self.target
            },
            "date": self.fake.date(pattern="%Y-%m-%d", end_datetime=None),
            "rate": self.fake.pyfloat(left_digits=1, right_digits=3, positive=True)
        }
        response = self.client.post('/forex/exchange/', json.dumps(data), content_type="application/json")
        self.assertEqual(response.status_code, 201)

        exchange_rate_history = ExchangeRateHistory.objects.latest('pk')
        response = self.client.get('/forex/history/?date={}'.format(exchange_rate_history.date))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(set(response.data[0].keys()), set(['id', 'exchange_rate_history', 'base', 'target', ]))
        self.assertEqual(set(response.data[0]['exchange_rate_history'][0].keys()), set(['id', 'weekly_average', 'date', 'rate', ]))

    def test_create_new_currency(self):
        data = {
            "base": self.base,
            "target": self.target
        }
        response = self.client.post('/forex/currency/', json.dumps(data), content_type="application/json")
        self.assertEqual(response.status_code, 201)

    def test_delete_currency(self):
        data = {
            "currency": {
                "base": self.base,
                "target": self.target
            },
            "date": self.fake.date(pattern="%Y-%m-%d", end_datetime=None),
            "rate": self.fake.pyfloat(left_digits=1, right_digits=3, positive=True)
        }
        response = self.client.post('/forex/exchange/', json.dumps(data), content_type="application/json")
        self.assertEqual(response.status_code, 201)

        data = {
            "base": self.base,
            "target": self.target
        }
        response = self.client.delete('/forex/currency/delete/', json.dumps(data), content_type="application/json")
        self.assertEqual(response.status_code, 204)

    def test_create_existing_currency(self):
        data = {
            "base": self.base,
            "target": self.target
        }
        response = self.client.post('/forex/currency/', json.dumps(data), content_type="application/json")
        self.assertEqual(response.status_code, 201)

        response = self.client.post('/forex/currency/', json.dumps(data), content_type="application/json")
        self.assertEqual(response.status_code, 400)

    def test_delete_unknown_currency(self):
        data = {
            "base": self.base,
            "target": self.target
        }
        response = self.client.delete('/forex/currency/delete/', json.dumps(data), content_type="application/json")
        self.assertEqual(response.status_code, 404)
