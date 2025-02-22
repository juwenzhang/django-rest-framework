from django.db import DatabaseError
from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.request import Request
from api import models
from _constant import comm


# 开始实现书写我们的一个类来作为我们的登录验证的
# 路径的参数校验认证模式
class UrlAuthentication(BaseAuthentication):
    def authenticate(self, request: Request):
        # 获取永固认证
        # 读取传递过来的 token
        # 检验 token 是否合法
        # 共有三种返回值
            # 返回元组  request.user  request.auth
            # 抛出异常: 实现我们的返回错误信息
            # 返回None  最后就是实现的是使用匿名用户
        # token = request._request.GET("token")
        token = request.query_params.get("token")
        if token:
            try:
                # 开始实现校验 token
                user_obj = models.UserInfo.objects.filter(token=token).first()
                if user_obj:
                    return user_obj, f"UrlAuthentication: {token}"
                    # 这两个值分贝是赋值给了我们的 request.user 和 request.auth
                    # 所以说在后面的视图函数中我们就可以实现的是来获取这两个属性来做一些事情了
                raise AuthenticationFailed(comm.AUTHENTICATION_USER_NOT_PASS_ERROR_MSG)
            except DatabaseError:
                raise AuthenticationFailed(comm.AUTHENTICATION_DATABASE_ERROR_MSG)
        else:
            return None # 实现的时候为了下面还可以继续处理我们就是使用的是 None 机制

    def authenticate_header(self, request: Request) -> str:
        return "UrlAuthentication"


# 请求头的校验认证模式
class HeaderAuthentication(BaseAuthentication):
    def authenticate(self, request: Request):
        token = request.META.get("HTTP_AUTHORIZATION")
        if token:
            try:
                # 开始实现校验 token
                user_obj = models.UserInfo.objects.filter(token=token).first()
                if user_obj:
                    return user_obj, f"HeaderAuthentication: {token}"
                    # 这两个值分贝是赋值给了我们的 request.user 和 request.auth
                    # 所以说在后面的视图函数中我们就可以实现的是来获取这两个属性来做一些事情了
                raise AuthenticationFailed(comm.AUTHENTICATION_USER_NOT_PASS_ERROR_MSG)
            except DatabaseError:
                raise AuthenticationFailed(comm.AUTHENTICATION_DATABASE_ERROR_MSG)
        else:
            return None

    def authenticate_header(self, request: Request) -> str:
        return "HeaderAuthentication"


class BodyAuthentication(BaseAuthentication):
    def authenticate(self, request: Request):
        token = request.data.get("token")
        print(token)
        if token:
            try:
                # 开始实现校验 token
                user_obj = models.UserInfo.objects.filter(token=token).first()
                if user_obj:
                    return user_obj, f"BodyAuthentication: {token}"
                    # 这两个值分贝是赋值给了我们的 request.user 和 request.auth
                    # 所以说在后面的视图函数中我们就可以实现的是来获取这两个属性来做一些事情了
                raise AuthenticationFailed(comm.AUTHENTICATION_USER_NOT_PASS_ERROR_MSG)
            except DatabaseError:
                raise AuthenticationFailed(comm.AUTHENTICATION_DATABASE_ERROR_MSG)
        else:
            return None

    def authenticate_header(self, request: Request) -> str:
        return "BodyAuthentication"


# 开始实现认证的不在进行处理的时候
class NoneAuthentication(BaseAuthentication):
    def authenticate(self, request: Request) -> AuthenticationFailed:
        raise AuthenticationFailed(comm.AUTHENTICATION_ALL_NOT_PASS_MSG)

    def authenticate_header(self, request: Request) -> str:
        return "NoneAuthentication"