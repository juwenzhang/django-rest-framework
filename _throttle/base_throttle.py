from rest_framework.throttling import SimpleRateThrottle
from django.core.cache import cache as default_cache

# 基本的限流组件
class Base_Throttle(SimpleRateThrottle):
    scope = "base-throttle"
    # THROTTLE_RATES = {"base-throttle": "5/min"}  # 访问频率
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


# 匿名用户限流组件
class IpThrottle(SimpleRateThrottle):
    # 开始书写我们的 ip 限流
    scope = "ip-throttle"
    # THROTTLE_RATES = {"ip_throttle": "3/m"}
    cache = default_cache

    def get_cache_key(self, request, view):
        ident = self.get_ident(request)  # 获取的是用户 ip 地址
        return self.cache_format % {"scope": self.scope, "ident": ident}

    def wait(self):
        return 180

    def get_throttle_message(self, request):
        wait_time = self.wait()
        return f"操作过于频繁，请在{wait_time}后进行重试"


# 具名用户的限流组件
class UserThrottle(SimpleRateThrottle):
    scope = "user-throttle"
    cache = default_cache

    def get_cache_key(self, request, view):
        user_id = request.user.pk
        return self.cache_format % {"scope": self.scope, "ident": user_id}

    def wait(self):
        return 300

    def get_throttle_message(self, request):
        wait_time = self.wait()
        return f"操作过于频繁，请在{wait_time}后进行重试"

