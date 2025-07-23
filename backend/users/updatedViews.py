from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import User
from .serializers import UserSerializer
from rest_framework import status

@api_view(['PUT'])
def user_update(request, id):
  try:
    user = User.objects.get(pk=id)
  except User.DoesNotExist:
    return Response(
      {"error": "Utilisateur non trouvé"},
      status=status.HTTP_404_NOT_FOUND
    )
  
  serializer = UserSerializer(user, data=request, partial=True)
  if serializer.is_valid():
    serializer.save()
    return Response(
      {"msg": "Utilisateur mis à jour avec succès", "data": serializer.data},
      status= status.HTTP_200_OK          
  )
  return Response(
    serializer.errors,
    status=status.HTTP_400_BAD_REQUEST
  )