from rest_framework import serializers
from django.contrib.auth.hashers import make_password
from rest_framework.decorators import authentication_classes, permission_classes

from .models import User


class UserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        # fields = "__all__"
        exclude = ["password"]


class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField(required=True)
    password = serializers.CharField(required=True)
    # class Meta:
    #     model = User
    #     fields = ('username', 'password')
        # read_only_fields = ('username', 'password')


class UserSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        password = validated_data.pop('password', None)
        # as long as the fields are the same, we can just use this
        instance = self.Meta.model(**validated_data)
        # check password before save to DB even password was secure in view.py though
        if password is not None:
            # instance method to save password to DB
            instance.set_password(password)
        instance.save()
        return instance

    def update(self, instance, validated_data):
        for attr, value in validated_data.items():
            # update all the attribute. But password need to update by this way
            if attr == 'password':
                instance.set_password(value)
            else:
                # set instance attribute atrr equal to value
                setattr(instance, attr, value)

        instance.save()
        return instance

    class Meta:
        model = User
        extra_kwargs = {'password': {'write_only': True}}
        # 'is_active', 'is_staff', 'is_superuser' is fields generate automatically by AbstractUser
        fields = ('id', 'username', 'password', 'info_id')
