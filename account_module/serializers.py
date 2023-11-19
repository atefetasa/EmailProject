from rest_framework import serializers
from .models import User
from django.db.models.signals import pre_save
from django.dispatch import receiver


# class UserRegisterSerializer(serializers.ModelSerializer):
#     password2 = serializers.CharField(write_only=True, required=True)
#
#     class Meta:
#         model = User
#         fields = ['username', 'password', 'password2', 'email', 'phone_number']
#         extra_kwargs = {
#             'password': {'write_only': True, 'validators': (clean_password,)},
#             'username': {'validators': (clean_username,)},
#             'phone_number': {'validators': (clean_phone_number,)}
#         }
#
#     def create(self, validated_data):
#         del validated_data['password2']
#         return User.objects.create_user(**validated_data)
#
#     @staticmethod
#     def check_password_matching(data):
#         if data['password'] != data['password2']:
#             raise serializers.ValidationError("password and password confirmation must match")
#         return data