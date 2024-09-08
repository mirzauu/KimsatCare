from django.contrib.auth import authenticate, login
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .serializers import LoginSerializer
from rest_framework.authtoken.models import Token  # If you are using Token Authentication

class LoginView(APIView):
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        email = serializer.validated_data.get('email')
        phone_number = serializer.validated_data.get('phone_number')
        password = serializer.validated_data.get('password')
        
        user = None
        if email:
            user = authenticate(request, email=email, password=password)
        
        if not user and phone_number:
            user = authenticate(request, phone_number=phone_number)

        if user:
            login(request, user)
            token, _ = Token.objects.get_or_create(user=user)
            return Response({"token": token.key}, status=status.HTTP_200_OK)
        else:
            return Response({"detail": "Invalid credentials."}, status=status.HTTP_401_UNAUTHORIZED)
