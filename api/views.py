import uuid
from django.db import DatabaseError
from django.http import QueryDict
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.versioning import QueryParameterVersioning
from rest_framework.parsers import JSONParser
from rest_framework.negotiation import DefaultContentNegotiation
from api import models
from _constant import comm
from api_view_temp.ProAPIView import ProAPIView
from _throttle.base_throttle import IpThrottle, UserThrottle
# from _permission.base_permission import MyPermission
# from _authentication.base_authentication import Base_Authentication

'''
每一个视图函数可以实现书写的认证方式可以为多个或者没有
没有的话就是不用进行任何校验
'''

"""
同时我们还是可以通过我们的全局配置来实现最终的确定我们的那些组件需要认证关系
"""

class LoginView(ProAPIView):
    # 通过定义静态变量的形式实现用户校验
    authentication_classes = []
    permission_classes = []
    throttle_classes = [UserThrottle, IpThrottle]
    versioning_class = QueryParameterVersioning
    parser_classes = [JSONParser, ]
    content_negotiation_class = DefaultContentNegotiation

    def get(self, request: Request, *args: tuple, **kwargs: dict) -> Response:
        return Response({
            "message": "欢迎来到 django-rest-framework project`s login page"
        })

    def post(self, request: Request, *args: tuple, **kwargs: dict) -> Response:
        # 开始实现我们的获取客户端信息
        # print(request._request.body)  django 的获取传输信息的方式
        # print(request.data)
        username: str = request.data.get("username")
        password: str = request.data.get("password")
        # 开始实现数据库用户校验
        if not username or not password:
            username: str = request.query_params.get("username")
            password: str = request.query_params.get("password")

        if not username or not password:
            return Response(comm.LOGIN_REQUEST_ERROR_MSG)

        try:
            user_obj: QueryDict = (models.UserInfo.objects.filter(
                username=username,
                password=password).
            first())

            user_obj_name = (models.UserInfo.objects.filter(
                username=username).
            first())

            if not user_obj_name:
                return Response(comm.LOGIN_USERNAME_ERROR_MSG)

            if not user_obj:
                return Response(comm.LOGIN_USER_ERROR_MSG)

            # 开始实现生成我们的 token
            token: str = user_obj.token
            if not token:
                token = str(uuid.uuid4())
                user_obj.token = token
                user_obj.save()

            return Response({
                "code": True,
                "msg": "登录成功",
                "token": token,
                "request_version": request.version
            })
        except DatabaseError:
            return Response(comm.LOGIN_DATABASE_ERROR_MSG)


class UserView(ProAPIView):
    # 通过定义静态变量的形式实现用户校验
    # authentication_classes = [Base_Authentication]
    def get(self, request: Request, *args: tuple, **kwargs: dict) -> Response:
        print(request.user.username, request.auth)
        return Response({
            "message": "欢迎来到 django-rest-framework project`s user page",
            "username": f"当前用户名称: {request.user.username}",
            "token": request.auth,
        })


class OrderView(ProAPIView):
    # 通过定义静态变量的形式实现用户校验
    # authentication_classes = [Base_Authentication]
    # permission_classes = [MyPermission, ]
    def get(self, request: Request, *args: tuple, **kwargs: dict) -> Response:
        print(request.user.username, request.auth)
        return Response({
            "message": "欢迎来到 django-rest-framework project`s order page",
            "username": f"当前用户名称: {request.user.username}",
            "token": request.auth,
        })


class DefaultView(ProAPIView):
    authentication_classes = []
    permission_classes = []
    def get(self, request: Request, *args: tuple, **kwargs: dict) -> Response:
        print(self.args, self.kwargs)
        return Response({
            "message": "欢迎来到 django-rest-framework project`s default page"
        })

