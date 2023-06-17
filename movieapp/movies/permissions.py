from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed for any request, so we'll always allow GET, HEAD, or OPTIONS requests.
        if request.method in ["GET", "POST" "HEAD", "PUT", "OPTIONS"]:
            return True

        # Check if the request user is the owner of the object
        return obj.user == request.user
