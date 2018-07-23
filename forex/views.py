from django.shortcuts import get_object_or_404
from models import Currency, ExchangeRateHistory
from serializers import CurrencySerializer, ExchangeRateHistorySerializer, CurrencyExchangeHistorySerializer
from rest_framework import viewsets


class CurrencyViewSet(viewsets.ModelViewSet):
    queryset = Currency.objects.all()
    serializer_class = CurrencySerializer

    def get_object(self, **kwargs):
        queryset = self.get_queryset()
        query_filter = dict()
        query_filter['base'] = self.request.data.get('base')
        query_filter['target'] = self.request.data.get('target')
        obj = get_object_or_404(queryset, **query_filter)
        self.check_object_permissions(self.request, obj)
        return obj


class CurrenctExchangeRateHistoryViewSet(viewsets.ModelViewSet):
    queryset = Currency.objects.all()
    serializer_class = CurrencyExchangeHistorySerializer


class ExchangeRateHistoryViewSet(viewsets.ModelViewSet):
    queryset = ExchangeRateHistory.objects.all()
    serializer_class = ExchangeRateHistorySerializer
