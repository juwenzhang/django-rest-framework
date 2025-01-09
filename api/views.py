import uuid
from rest_framework.response import Response
from rest_framework.views import APIView
from api import models
# from _authentication.base_authentication import Base_Authentication

'''
每一个视图函数可以实现书写的认证方式可以为多个或者没有
没有的话就是不用进行任何校验
'''

"""
同时我们还是可以通过我们的全局配置来实现最终的确定我们的那些组件需要认证关系
"""

class LoginView(APIView):
    # 通过定义静态变量的形式实现用户校验
    authentication_classes = []
    def get(self, request):
        return Response({
            "message": "欢迎来到 django-rest-framework project"
        })

    def post(self, request, *args, **kwargs):
        # 开始实现我们的获取客户端信息
        # print(request._request.body)  django 的获取传输信息的方式
        # print(request.data)
        username = request.data.get("username")
        password = request.data.get("password")
        # 开始实现数据库用户校验
        user_obj = models.UserInfo.objects.filter(username=username, password=password).first()
        if not user_obj:
            return Response({
                "code": False,
                "msg": "用户名不存在或密码错误"
            })
        # 开始实现生成我们的 token
        token = user_obj.token
        if not token:
            token = str(uuid.uuid4())
            user_obj.token = token
            user_obj.save()

        return Response({
            "code": True,
            "msg": "登录成功",
            "token": token
        })


class UserView(APIView):
    # 通过定义静态变量的形式实现用户校验
    # authentication_classes = [Base_Authentication]
    def get(self, request):
        print(request.user.username, request.auth)
        return Response({
            "message": "欢迎来到 django-rest-framework project",
            "username": "",
            "token": request.auth,
        })


class OrderView(APIView):
    # 通过定义静态变量的形式实现用户校验
    # authentication_classes = [Base_Authentication]
    def get(self, request):
        print(request.user.username, request.auth)
        return Response({
            "message": "欢迎来到 django-rest-framework project",
            "username": f"当前用户名称: {request.user.username}",
            "token": request.auth,
        })


class DefaultView(APIView):
    def get(self, request, *args, **kwargs):
        print(self.args, self.kwargs)
        return Response({
            "message": "欢迎来到 django-rest-framework project"
        })

