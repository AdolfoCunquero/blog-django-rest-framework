from rest_framework.permissions import BasePermission

class isAdminOrReadAll(BasePermission):
    def has_permission(self, request, view):
        #return super().has_permission(request, view)
        if request.method == 'GET':
            return True

        else:
            return request.user.is_staff