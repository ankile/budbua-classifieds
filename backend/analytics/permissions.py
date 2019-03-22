from rest_framework.permissions import IsAuthenticated


class IsOwner(IsAuthenticated):
    """
    Allows access only to authenticated users.
    """

    def has_permission(self, request, view):
        return super().has_permission(request, view) and \
               'Owner' in map(lambda g: g.name, request.user.groups.all())
