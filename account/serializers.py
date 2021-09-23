from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Account

class AccountSerializer(serializers.ModelSerializer):
    class Meta:
      model = Account
      fields = (
          "birth_date",
          "phone",
          "address1",
          "address2",
          "zip_code",
          "city",
          "country"
      )


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
        read_only_fields = ['password']
        # extra_kwargs = {'password': {"write_only": True, 'required': True}}

    # Override built-in create method to create Account object as well
    def create(self, validated_data):
        account_data = validated_data.pop('account')
        user = User.objects.create_user(**validated_data)
        user.account = Account.objects.create(user=user, **account_data)
        user.save()
        return user

    def update(self, instance, validated_data):
        account_data = validated_data.pop('account')
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.email = validated_data.get('email', instance.email)
        instance.account.birth_date = account_data.get('birth_date', instance.account.birth_date)
        instance.account.phone = account_data.get('phone', instance.account.phone)
        instance.account.address1 = account_data.get('address1', instance.account.address1)
        instance.account.address2 = account_data.get('address2', instance.account.address2)
        instance.account.zip_code = account_data.get('zip_code', instance.account.zip_code)
        instance.account.city = account_data.get('city', instance.account.city)
        instance.account.country = account_data.get('country', instance.account.country)
        instance.save()
        return instance

