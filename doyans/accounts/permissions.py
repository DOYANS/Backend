from rest_framework.permissions import BasePermission

# create permissions

class DoyansUserJWTPermission(BasePermission):
    '''
    user can see self details
    only admins can see all user details
    '''

    def has_permission(self, request, view):
        
        if request.user.is_super_user:
            return True

        if request.user.is_authenticated:
            return True
        
        return False

    def has_object_permission(self, request, view, obj):

        if request.user.is_super_user:
            return True

        if obj.username == request.user.username:
            return True

        return False
