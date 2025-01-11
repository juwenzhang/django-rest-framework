from rest_framework.throttling import SimpleRateThrottle
from django.core.cache import cache as default_cache

class MyThrottle(SimpleRateThrottle):
    scope = "my-throttle"
    THROTTLE_RATES = {"my-throttle": "5/min"}  # 访问频率
    cache = default_cache

    # 实现获取节流认证的唯一标识
    def get_cache_key(self, request, view):
        if request.user:
            ident = request.user.pk  # 注意在我们的节流认证前默认已经执行过了认证校验和权限校验了的
        else:
            ident = self.get_ident(request)  # 获取的是用户 ip 地址
        return self.cache_format % {"scope": self.scope, "ident": ident}

    def wait(self):
        return 60

    def get_throttle_message(self, request):
        return "你的请求过于频繁，请在 %d 秒后重试" % self.wait()