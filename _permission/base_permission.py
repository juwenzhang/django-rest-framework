import random
from rest_framework.request import Request
from rest_framework.permissions import BasePermission
from _constant import comm

class MyPermission(BasePermission):
    message = comm.PERMISSION_NOT_PASS_MSG

    def has_permission(self, request: Request, view):
        # 实现重写父类
        print(request.user.username, request.auth)
        v1 = random.randint(1, 10)
        if v1 == 2:
            return True
        return False