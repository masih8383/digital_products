from rest_framework import serializers
from payments.models import Payment,Gateway



class GatewaySerializer(serializers.ModelSerializer):
    class Meta:
        model = Gateway
        fields ='all'



class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields ='all'

