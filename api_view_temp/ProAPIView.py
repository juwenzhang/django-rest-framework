from rest_framework.views import APIView

class ProAPIView(APIView):
    def check_permissions(self, request):
        not_have_permission_objects = []
        for _permission in self.get_permissions():
            if _permission.has_permission(request, self):
                return
            else:
                not_have_permission_objects.append(_permission)

        if len(not_have_permission_objects) > 0:
            self.permission_denied(
                request,
                message=getattr(not_have_permission_objects[0], "message", None),
                code=getattr(not_have_permission_objects[0], "code", None)
            )

