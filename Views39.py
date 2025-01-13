from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated

# Admin Login View
@api_view(['POST'])
def admin_login_view(request):
    username = request.data.get('username')
    password = request.data.get('password')

    if not username or not password:
        return Response({"detail": "Username and password are required."}, status=status.HTTP_400_BAD_REQUEST)

    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_staff:  # Check if the user is an Admin
            return Response({"detail": "Admin login successful!"}, status=status.HTTP_200_OK)
        else:
            return Response({"detail": "Not authorized. Only Admins can access admin pages."}, status=status.HTTP_403_FORBIDDEN)
    else:
        return Response({"detail": "Invalid credentials."}, status=status.HTTP_401_UNAUTHORIZED)


# Employee Login View
@api_view(['POST'])
def employee_login_view(request):
    username = request.data.get('username')
    password = request.data.get('password')

    if not username or not password:
        return Response({"detail": "Username and password are required."}, status=status.HTTP_400_BAD_REQUEST)

    user = authenticate(username=username, password=password)
    if user is not None:
        if not user.is_staff:  # Ensure the user is not an Admin
            return Response({"detail": "Employee login successful!"}, status=status.HTTP_200_OK)
        else:
            return Response({"detail": "Not authorized. Admins cannot access employee pages."}, status=status.HTTP_403_FORBIDDEN)
    else:
        return Response({"detail": "Invalid credenti
als."}, status=status.HTTP_401_UNAUTHORIZED)
For this view do I need to add model??
