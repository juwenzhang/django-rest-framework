import uuid
from django.db import DatabaseError
from django.http import QueryDict, HttpRequest
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.versioning import QueryParameterVersioning
from rest_framework.parsers import JSONParser
from rest_framework.negotiation import DefaultContentNegotiation
from api import models
from api.serilizer import UserInfoSerializer
from _constant import comm
from _throttle.base_throttle import IpThrottle, UserThrottle
from api_view_temp.ProAPIView import ProAPIView
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
        data = request.data
        # 开始实现数据库用户校验
        if not username or not password:
            username: str = request.query_params.get("username")
            password: str = request.query_params.get("password")
            data = request.query_params

        # if not username or not password:
        #     return Response(comm.LOGIN_REQUEST_ERROR_MSG)
        ser = UserInfoSerializer.UserInfoSerializerPost(data=data)
        if ser.is_valid():
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
        else:
            return Response(ser.errors)

class RegisterView(ProAPIView):
    authentication_classes = []
    permission_classes = []
    throttle_classes = [IpThrottle]
    versioning_class = QueryParameterVersioning
    parser_classes = [JSONParser, ]
    content_negotiation_class = DefaultContentNegotiation

    def post(self, request):
        username: str = request.query_params.get("username")
        password: str = request.query_params.get("password")
        data = request.query_params
        if not username or not password or not data:
            username: str = request.data.get("username")
            password: str = request.data.get("password")
            data = request.data

        # if not username or not password:
        #     return Response(comm.LOGIN_REQUEST_ERROR_MSG)
        # 开始实现校验用户名是否存在
        ser = UserInfoSerializer.UserInfoSerializerPost(data=data)
        if ser.is_valid():
            print(ser.validated_data)
            try:
                user_obj = models.UserInfo.objects.filter(username=username).first()
                if user_obj:
                    return Response(comm.REGISTER_HAVE_META_ERROR)

                (models.UserInfo.objects.create(
                    username=username,
                    password=password).
                save())

                return Response({
                    "status": True,
                    "msg": "注册成功",
                    "redirect": "/login"
                })
            except DatabaseError:
                return Response({
                    "code": 500,
                    "status": True,
                    "msg": "服务器内部出错"
                })
        else:
            return Response(ser.errors)

class DetailView(ProAPIView):
    permission_classes = []
    throttle_classes = []
    versioning_class = QueryParameterVersioning
    def get(self, request):
        try:
            # user_obj = (models.UserInfo.objects.filter(
            #     username=request.user.username)
            # .first())
            user_objs = models.UserInfo.objects.all()
            ser = UserInfoSerializer.UserInfoSerializerGet(
                instance=user_objs,
                many=True
            )
            # print(ser.data)
            return Response({
                "status": True,
                "data": [
                    ser.data
                ]
            })
        except DatabaseError:
            return Response({
                "status": False,
                "data": [],
                "msg": "服务器内部错误",
                "code": 500
            })

class UserView(ProAPIView):
    versioning_class = QueryParameterVersioning
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
    versioning_class = QueryParameterVersioning
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
    versioning_class = QueryParameterVersioning
    authentication_classes = []
    permission_classes = []
    def get(self, request: Request, *args: tuple, **kwargs: dict) -> Response:
        print(self.args, self.kwargs)
        return Response({
            "message": "欢迎来到 django-rest-framework project`s default page"
        })