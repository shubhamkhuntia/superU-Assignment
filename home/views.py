from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from home.models import UserProfile
from home.serializers import UserSerializer, LoginSerializer, RegisterSerializer
from rest_framework.authentication import TokenAuthentication
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated


class LoginAPI(APIView):

    def post(self, request):
        data = request.data
        serializer = LoginSerializer(data=data)

        if not serializer.is_valid():
            return Response({
                'status': False,
                'message': serializer.errors
            }, status.HTTP_400_BAD_REQUEST)

        user = authenticate(
            username=serializer.data['username'], password=serializer.data['password'])

        if not user:
            return Response({
                'status': False,
                'message': 'invalid credentials'
            }, status.HTTP_400_BAD_REQUEST)

        token, _ = Token.objects.get_or_create(user=user)

        return Response({
            'status': True,
            'message': 'user logged in',
            'token': str(token)
        }, status.HTTP_201_CREATED)


class RegisterAPI(APIView):

    def post(self, request):
        data = request.data
        serializer = RegisterSerializer(data=data)

        if not serializer.is_valid():
            return Response({
                'status': False,
                'message': serializer.errors
            }, status.HTTP_400_BAD_REQUEST)

        serializer.save()

        return Response({
            'status': True,
            'message': 'user created',
        }, status.HTTP_201_CREATED)


@api_view(['POST'])
def login(request):
    data = request.data
    serializer = LoginSerializer(data=data)

    if serializer.is_valid():
        data = serializer.validated_data
        return Response({'message': 'Logged Sucesssfully'})

    return Response(serializer.errors)


@api_view(['GET', 'POST', 'PATCH'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
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
