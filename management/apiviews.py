import random
import kavenegar

from django.http import HttpResponse
from django.shortcuts import redirect
from zeep import Client

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.status import HTTP_200_OK
from rest_framework.permissions import AllowAny

from django.contrib.auth import login, authenticate
from django.contrib.auth.hashers import check_password
from .models import User

from . import models
from . import serializers


class Register(APIView):

    permission_classes = [AllowAny]

    def post(self, request):
        phonenumber = request.data.get('phonenumber', '').strip()
        if phonenumber == '':
            return Response(0)

        while True:
            key = random.randint(100000, 999999)
            count = models.SMSVerification.objects.filter(verification_code=key).count()
            if count == 0:
                break

        # KaveNegar
        api = kavenegar.KavenegarAPI('586277556D2B396E636E727437305746414950323050326B57524654744B3930546E4157612F556C714C673D')
        params = {'sender': '1000596446', 'receptor': phonenumber, 'message': key}
        response = api.sms_send(params)

        verification = models.SMSVerification(phone_number=phonenumber, verification_code=key)
        verification.save()

        return Response(1)


class RegisterConfirm(APIView):

    permission_classes = [AllowAny]

    def post(self, request):
        phonenumber = request.data.get('phonenumber', '')
        code = request.data.get('code', '').strip()
        # if phonenumber == '':
        #     return Response('0')
        # obj = models.SMSVerification.objects.filter(verification_code=code, phone_number=phonenumber)
        obj = models.SMSVerification.objects.filter(verification_code=code)
        if obj.count() == 0:
            return Response(0)

        obj = User.objects.filter(phone_number=phonenumber)
        if obj.count() == 0:
            user = User(username=phonenumber, email=phonenumber)
            user.set_password(phonenumber)
            user.is_staff = True
            user.phone_number = phonenumber
            user.save()

        user = authenticate(request, username=phonenumber, password=phonenumber)
        if user:
            token, _ = Token.objects.get_or_create(user=user)
            return Response({'token': token.key}, status=HTTP_200_OK)
        else:
            return Response(0)


class Profile(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        phonenumber = request.GET.get('phonenumber', '')

        user = models.User.objects.filter(phone_number=phonenumber)
        if user.count() > 0:
            username = user[0].username
            phonenumber = user[0].phone_number
            email = user[0].email
            money = user[0].money

            return Response({'username': username, 'phonenumber': phonenumber, 'email': email, 'money': money})

        return Response(0)

    def post(self, request):
        phonenumber = request.data.get('phonenumber', '')

        username = request.data.get('username', '')
        email = request.data.get('email', '')

        print(username)
        print(email)

        user = models.User.objects.get(phone_number=phonenumber)
        user.email = email
        user.username = username
        user.save()

        return Response(1)


class Logout(APIView):
    def get(self, request):

        request.user.auth_token.delete()
        return Response(1, status=HTTP_200_OK)


class Withdraw(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        phonenumber = request.data.get('phonenumber', '')
        card_number = request.data.get('cardnumber', '')
        name = request.data.get('name', '')

        user = models.User.objects.get(phone_number=phonenumber)

        if user != None:
            withdraw = models.Withdraw()
            withdraw.user = user
            withdraw.name = name
            withdraw.card_number = card_number
            withdraw.money = user.money
            withdraw.save()

            user.money = 0
            user.save()
            return Response(1)
        return Response(0)


class ChargeAccount(APIView):

    permission_classes = [AllowAny]

    def get(self, request):
        amounts = models.ChargePlaceHolder.objects.all()
        serialized_data = serializers.ChargePlaceHolderSerializer(amounts, many=True)
        data = serialized_data.data
        return Response(data)


class Roles(APIView):

    permission_classes = [AllowAny]

    def get(self, request):
        roles = models.Roles.objects.all()
        serialized_data = serializers.RolesSerializer(roles, many=True)
        data = serialized_data.data
        return Response(data)


class StreamURL(APIView):

    permission_classes = [AllowAny]

    def get(self, request):
        stream = models.Stream.objects.all()
        stream = stream[0]
        serialized_data = serializers.StreamSerializer(stream)
        data = serialized_data.data
        return Response(data)


class Player(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        phonenumber = request.GET.get('phonenumber', '')

        player = models.User.objects.get(phone_number=phonenumber)
        serialized_data = serializers.PlayerData(player)
        data = serialized_data.data
        return Response(data)
