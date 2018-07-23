import views

from rest_framework import routers

router = routers.DefaultRouter(trailing_slash=True)
router.register(r'currency', views.CurrencyViewSet)
router.register(r'history', views.CurrenctExchangeRateHistoryViewSet)
router.register(r'exchange', views.ExchangeRateHistoryViewSet)

urlpatterns = router.urls
