from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny
from .models import User
from .serializers import UserSerializer

@api_view(['PUT'])
@permission_classes([AllowAny])
def user_update(request, id):
    try:
        user = User.objects.get(pk=id)
    except User.DoesNotExist:
        return Response(
            {"error": "Utilisateur non trouvé"},
            status=status.HTTP_404_NOT_FOUND
        )

    serializer = UserSerializer(user, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(
            {"msg": "Utilisateur mis à jour avec succès", "data": serializer.data},
            status=status.HTTP_200_OK
        )
    return Response(
        serializer.errors,
        status=status.HTTP_400_BAD_REQUEST
    )