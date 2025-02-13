from django.urls import path
from .models import Package, Subscription
from .views import PackageView,SubscriptionView

urlpatterns = [
     path('package/', PackageView.as_view(), name='package'),
     path('subscription/', SubscriptionView.as_view(), name='subscription'),

 ]