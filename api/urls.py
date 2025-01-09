from django.urls import path
from api import views

# 开始实现开发我们的 api 接口的路由匹配了
urlpatterns = [
    path("login/", views.LoginView.as_view()),
    path("user/", views.UserView.as_view()),
    path("order/", views.OrderView.as_view()),
    path("default/<int:version>/<int:id>/", views.DefaultView.as_view()),
]