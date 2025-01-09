from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

"""
使用原生的 django 实现我们的前后端开发模式、
只是需要返回我们的 JsonResponse 即可
但是这样的话只是方便我们的 get 请求的前后端开发
对于我们的 post 请求是很不好进行处理的
"""
def auth(request) -> JsonResponse:
    return JsonResponse({
        "status": "ok",
        "message": "success"
    })


"""
开始使用我们的 rest_framework 实现我们的前后端分离的开发
"""
@api_view(["GET"])
def login(request) -> Response:
    return Response({
        "status": "ok",
        "message": "success"
    })


class LoginView(APIView):
    def get(self, request) -> Response:
        return Response({
            "status": "ok",
            "message": "success"
        })

class InfoView(APIView):
    def get(self, request, *args, **kwargs) -> Response:
        return Response({
            "status": "ok",
            "message": "success"
        })

    def post(self, request) -> Response:
        return Response({
            "status": "ok",
            "message": "success"
        })

    def put(self, request) -> Response:
        return Response({
            "status": "ok",
            "message": "success"
        })

    def delete(self, request) -> Response:
        return Response({
            "status": "ok",
            "message": "success"
        })
