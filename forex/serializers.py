from datetime import timedelta
from django.db.models import Avg
from models import Currency, ExchangeRateHistory
from rest_framework import serializers


class CurrencySerializer(serializers.ModelSerializer):

    class Meta:
        model = Currency
        fields = '__all__'


class ExchangeRateHistorySerializer(serializers.ModelSerializer):
    currency = CurrencySerializer(validators=[])
    weekly_average = serializers.SerializerMethodField()

    class Meta:
        model = ExchangeRateHistory
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        remove_fields = kwargs.pop('remove_fields', None)
        super(ExchangeRateHistorySerializer, self).__init__(*args, **kwargs)

        if remove_fields:
            # for multiple fields in a list
            for field_name in remove_fields:
                self.fields.pop(field_name)

    def create(self, validated_data):
        currency, created = Currency.objects.get_or_create(base=validated_data['currency']['base'], target=validated_data['currency']['target'])
        currency.base = validated_data['currency']['base']
        currency.target = validated_data['currency']['target']
        currency.save()

        exchange_history, created = ExchangeRateHistory.objects.get_or_create(
            currency=currency, date=validated_data['date']
        )
        exchange_history.date = validated_data['date']
        exchange_history.rate = validated_data['rate']
        exchange_history.save()
        return exchange_history

    def get_weekly_average(self, obj):
        one_week_ago = obj.date - timedelta(days=7)
        weekly_avg = ExchangeRateHistory.objects.filter(date__gt=one_week_ago, date__lte=obj.date, currency=obj.currency).values('currency').annotate(Avg('rate'))

        return weekly_avg


class CurrencyExchangeHistorySerializer(serializers.ModelSerializer):
    exchange_rate_history = serializers.SerializerMethodField()

    class Meta:
        model = Currency
        fields = '__all__'

    def get_exchange_rate_history(self, obj):
        exchange_rate_history = ExchangeRateHistory.objects.filter(currency__id=obj.pk)
        date_filter = self.context['request'].query_params.get('date', None)
        if date_filter is not None:
            exchange_rate_history = exchange_rate_history.filter(date=date_filter)
        return ExchangeRateHistorySerializer(exchange_rate_history, many=True, remove_fields=['currency']).data
