import uuid
import random
from django.core.cache import cache
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import User,Device


class RegisterView(APIView):

    def post(self, request):
        phone_number = request.data.get('phone_number')
        if not phone_number:
            return Response( status=status.HTTP_400_BAD_REQUEST)
        try:
            user = User.objects.get(phone_number=phone_number)
        except User.DoesNotExist:
            user = User.objects.create_user(phone_number=phone_number)
            return Response({'detail': 'User already exists'},
                            status=status.HTTP_400_BAD_REQUEST)
        #user, created = User.objects.get_or_create(phone_number=phone_number)



        device = Device.objects.create(user=user)

        code = random.randint(10000,99999)
        #chache
        cache.set(str(phone_number), code, 2*60)
        return Response({'code': code})


class GetToken(APIView):
    def post(self, request):
        phone_number = request.data.get('phone_number')
        code = request.data.get('code')

        cached_code = cache.get(str(phone_number))

        if code != cached_code:
            return Response(status=status.HTTP_401_UNAUTHORIZED)

        token=str(uuid.uuid4())
        return Response({'token':token})