from django.db import models

# Create your models here.
class UserInfo(models.Model):
    username = models.CharField(verbose_name="用户名", max_length=20)
    password = models.CharField(verbose_name="密码", max_length=20)
    # redis 或者 jwt 也是可以的
    token = models.CharField(verbose_name="TOKEN", max_length=64, null=True, blank=True)
