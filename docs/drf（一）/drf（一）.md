# drf（一）

**https://www.django-rest-framework.org/**

## 前后端分离

* 从程序的角度而言的话：
  * 我们以前的开发模式中，我们的开发都是通过我们的 django 来实现的，django 程序实现处理了我们的视图，模板，数据库操作
    * 这种开发模式就是我们的前后端未分离的开发模式
    * 这个时候我们的一个 django 程序就是整个程序的处理代码逻辑了
  * 前后端分离的开发模式：就是实现的是我们的前端一套代码，后端一套代码的基本形式
    * 这个时候我们的项目部署就需要进行的是分开部署了
    * 一个是前端**静态资源服务器**的部署
    * 一个是后端 **api** 的部署
    * 这个时候我们的开发就是十分有效的了，专业的人干专业的活
    * 同时前后端分离还具备的其他有点
      * 后端注重于对数据的处理
      * 可以实现多套客户端共同使用一套后端代码来实现的优点了
      * 在该过程中主要是使用我们的 JSON 的数据格式实现数据的返回
    * 这个时候就出来一些框架可以使用来适应我们的前后端分离的开发模式
      * **django + django-restframework**
      * **django + django-ninjia**
      * **flask**
      * **fastapi**
* 前后端代码的**单独部署**
  * 就是将我们的静态资源前端实现部署在我们的静态资源服务器中，浏览器或者说客户端实现访问的就是静态资源服务器的地址了
  * 在这个过程中我们的静态资源服务器的数据是来自于我们的后端 **api** 中的，所以说前端就发送网络请求，获取数据，渲染前端

![def01](.\drf01.png)

## drf 的作用是什么呐？？

* drf 就是我们的一个在 django 基础上的一个框架，可以更加适用于我们的现在的 **restful** 的开发模式
  * **pip install django**
  * **pip install djangorestframework**
* 在我们现在的前后端开发模式中，我们需要进行的就是学会使用 **postman** **apifox** **apipost** 的 api 调试工具
* 首先我们进行开发程序之前首先需要做的就是进行创建虚拟环境
  * **mkvirtualenv env_name**
  * **workon env_name**
  * **django-admin startproject project_name .** 和以前的创建项目有所不同，这里直接使用的是在本级目录进行创建的项目
  * **cd project_name**
  * **python manage.py startapp app01**
* 这个时候为了前后端分离的开发模式实现我们的开发，所以说我们就需要进行的是返回 JsonResponse 字符串的开发模式
  * **from django.http import JsonResponse**
  * 这是我们不使用 **djangorestframework** 的开发模式，就是直接使用我们的返回数据即可
* 首先我们先声明一点的是：
  * **piip install djangorestframework**
  * 该应用本身就是一个 **django app** 
  * 所以说我们还是需要**进行配置文件的注册**的呐
    * 注册信息是： **rest_framework**
  * **from rest_framework.response import Response**
  * 这个时候就是通过我们的该方法实现返回我们的数据了
    * 这样之后返回的页面是比原本的页面好看一些的，便于开发的观看的
    * 同时注意配置文件的修改

```python
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
```

```python
"""def_pro URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from app01 import views

urlpatterns = [
    path('auth/', views.auth),
    path('login/', views.login),
    # path('login/', views.LoginView.as_view())
]
```

![drf02](.\drf02.png)

## drf 的 FBV 和 CBV

* **FBV**
  * 就是我们的基于函数的视图函数的书写
  * 对于原生的django 的只需要只需要进行书写函数即可
  * 但是在我们的 rest_framework 中的时候就需要给视图函数添加装饰器 **@api_view["GET"]** 
* **CBV**
  * 就是通过类书写的视图函数的实现
  * 我们的CBV 在我们的django 中实现 CBV 的书写，视图函数需要继承的的是 **django.views.View** 
  * 但是在我们的 rest_framework 中实现书写CBV ，视图函数需要继承的就是 **rest_framework.views.APIView**
  * 但是最后在进行我们的后端路由的注册的时候都是需要进行我们的 **as_view()** 转化视图函数的
    * 在源码中有对请求方式判断的 **lower()** 函数的书写，所以说，就忽略了大小写
    * 但是我们在视图函数中的书写还是尽量使用我们的大写才可
* **@csrf_exempt** 实现的是为我们的视图函数免除 **csrf_token** 的装饰器 
  * 这里就涉及了前后端分离和不分离的效果了
    * 实际上的话在我们的额 rest 中所有的视图中的话就没有我们的 token 校验了
    * 以前的是通过模板视图传递 **csrf_token** 的传递实现的我们的前端获取 **token** 的
  * 在前后端未分离的情况下，我们服务端直接进行在未分离的首次请求进行获取并且保存 **token** 的
    * 但是分离后，我们的 **token** 就是实现的是我们的就没有 **token** 校验了
    * 前后端分离后不再进行返回页面了，就无法实现使用我们的 **token** 限制了
    * 这个时候就含有了我们的 **jwt** 认证了

* 对于我们的 **rest_framework** 中的实现效果就是
  * 本质上的话 **APIView**
    * 帮助我们实现免除了 **csrf_token** 的验证方式
    * 同时内部底层源码的话帮助我们进行了 **dispatch** 的视图执行之前和视图执行后的处理
* 同时在我们的前后端参数的时候具有我们的
  * 可选参数和必须参数
    * 可选参数就是我们的 ***args** 或者 **kwargs**
    * 如果是我们的必须参数，就需要进行的是我们的把每个参数写全，来代表我们的可选参数

```python
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
```

