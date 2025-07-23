from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404

@api_view(['DELETE'])
def delete_profile(request, user_id):
        user = get_object_or_404(User, id=user_id)
        
        if request.user != user:
            return Response(
            {"error": "Vous n'avez pas la permission de supprimer ce profil."},
            status=status.HTTP_403_FORBIDDEN
        )
        
        user.delete()

        return Response(
        {"message": "Profil supprimé !"},
        status=status.HTTP_204_NO_CONTENT
    )
