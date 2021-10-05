from rest_framework import serializers
# DjangoのデフォルトのUserモデルを利用
from django.contrib.auth.models import User
from .models import Book


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'username', 'password')
        # パスワードはwrite_only(入力できるが、readできない設定)と入力を必須にする
        extra_kwargs = {'password': {'write_only': True, 'required': True}}

    def create(self, validated_data):
        # Djangoに用意されているcreate_userメソッドを使って、
        # 新しくユーザーを作成(通常のserializerのcreateではパスワードが暗号化されないため)
        user = User.objects.create_user(**validated_data)
        return user


class BookSerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", read_only=True)

    class Meta:
        model = Book
        fields = ('id', 'title', 'author', 'image', 'caption', 'itemUrl', 'created_at')
