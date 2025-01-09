from django.test import TestCase

# Create your tests here.
class Obj01:
    def get(self):
        print("我是 get 请求")

    def post(self):
        print("我是 post 请求")

class Obj:
    def __init__(self):
        self._obj01 = Obj01()
        self._data = 10

    def __getattr__(self, attr):
        try:
            return getattr(self._obj01, attr)
        except AttributeError as e:
            return self.__getattribute__(attr)