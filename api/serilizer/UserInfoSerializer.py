from uuid import uuid4
from rest_framework import serializers, exceptions
from api import models


# get 请求校验序列化器校验
class UserInfoSerializerGet(serializers.ModelSerializer):
    # 这个时候继承的是 serializer.S~~~
    # username = serializers.CharField()
    # password = serializers.CharField()
    # token = serializers.CharField()

    # 在这里可以实现的是自定义数据的字段的
    # 都是可以的，随意吧，官方文档有很多种
    # 书写的话就是为了区分一些枚举 | 外键字段 等就使用我们的自定义字段进行返回即可
    # fields 就是进行的我们的设置返回那些字段进行序列化吧
    # model 就是设置的我们的需要根据哪一个表进行序列化操作
    other_data = serializers.SerializerMethodField()

    class Meta:
        model = models.UserInfo
        fields = ["username", "token", "other_data"]

    def get_other_data(self, obj):
        return f"other_data-{uuid4()}"


# post 请求校验序列化器校验
class UserInfoSerializerPost(serializers.Serializer):
    username = serializers.CharField(required=True)
    password = serializers.CharField(required=True)

    def validate_username(self, value):
        if len(value) < 6 or len(value) > 20:
            raise exceptions.ValidationError("用户名不能超过6位或者不能超过20位~~~~")
        return value

    def validate_password(self, value):
        length = len(value)
        if length < 6 or length > 32:
            raise exceptions.ValidationError("密码不能超过6位或者不能超过20位~~~~")

        if 6 <= length < 10:
            return "密码不安全"

        if 10 <= length < 20:
            return "密码中等"

        if 20 <= length < 25:
            return "密码安全"

        if 25 <= length <= 32:
            return "密码灰常安全"

    def validate(self, attrs):
        return attrs