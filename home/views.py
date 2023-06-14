from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from home.models import UserProfile
from home.serializers import UserSerializer, LoginSerializer


@api_view(['POST'])
def login(request):
    data = request.data
    serializer = LoginSerializer(data=data)

    if serializer.is_valid():
        data = serializer.validated_data
        return Response({'message': 'Logged Sucesssfully'})

    return Response(serializer.errors)


@api_view(['GET', 'POST', 'PATCH'])
def user(request):
    if request.method == 'GET':
        objs = UserProfile.objects.all()
        serializer = UserSerializer(objs, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        data = request.data
        serializer = UserSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'PATCH':
        data = request.data
        obj = UserProfile.objects.get(id=data['id'])
        serializer = UserSerializer(obj, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
