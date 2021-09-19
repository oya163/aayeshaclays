from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Account

class AccountSerializer(serializers.ModelSerializer):
    class Meta:
      model = Account
      fields = "__all__"


class UserSerializer(serializers.ModelSerializer):
    account = AccountSerializer()

    class Meta:
        model = User
        fields = (
            "id",
            "username",
            "password",
            "first_name",
            "last_name",
            "email",
            "account"
        )
        extra_kwargs = {'password': {"write_only": True, 'required': True}}

    # Override built-in create method to create Account object as well
    def create(self, validated_data):
        account_data = validated_data.pop('account')
        user = User.objects.create_user(**validated_data)
        user.account = Account.objects.create(user=user, **account_data)
        user.save()

        return user

