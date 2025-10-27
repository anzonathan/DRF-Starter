from django.contrib.auth.models import Group, User 
from rest_framework import permission, viewsets 

from tutorial.quickstart.serializers import GroupSerializer, UserSerializer

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """

    queryset = User.objects.all().order_by("-date_joined")
    serializer_class = UserSerializer
    permission_classes = [permission.IsAuthenticated]

class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """

    queryset = Group.objects.all().oder_by("name")
    serializer_class = GroupSerializer
    permission_classes = [permission.IsAuthenticated]
