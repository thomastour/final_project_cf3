from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        
        if request.method in ["GET", "POST" "HEAD", "PUT", "OPTIONS"]:
            return True

        # Check if the request user is the owner of the object
        return obj.user == request.user
