from rest_framework import serializers
from subscriptions.models import Package, Subscription


class PackageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Package
        fields = ('title','sku','description','avator','price','duration')




class SubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscription
        fields=('package','created_time' ,'expire_time')









