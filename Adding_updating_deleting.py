# employees/views.py

from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from .models import Employee
from .serializers import EmployeeSerializer
from django.contrib.auth.models import User


# Only Admins can access these views, hence permission_classes ensures only admin can use them.

# Add a new employee (Admin only)
@api_view(['POST'])
@permission_classes([IsAuthenticated])  # Only authenticated users
def add_employee(request):
    if not request.user.is_staff:
        return Response({"detail": "Permission Denied. Admins only."}, status=status.HTTP_403_FORBIDDEN)

    # Create employee linked to user
    username = request.data.get('username')
    password = request.data.get('password')
    department = request.data.get('department')
    position = request.data.get('position')
    date_of_joining = request.data.get('date_of_joining')

    # Create new User
    user = User.objects.create_user(username=username, password=password)
    
    # Create Employee record
    employee = Employee.objects.create(user=user, department=department, position=position, date_of_joining=date_of_joining)
    
    serializer = EmployeeSerializer(employee)
    return Response({"detail": "Employee created successfully.", "employee": serializer.data}, status=status.HTTP_201_CREATED)


# Update an employee's details (Admin only) using PATCH
@api_view(['PATCH'])
@permission_classes([IsAuthenticated])
def update_employee(request, employee_id):
    if not request.user.is_staff:
        return Response({"detail": "Permission Denied. Admins only."}, status=status.HTTP_403_FORBIDDEN)

    try:
        employee = Employee.objects.get(id=employee_id)
    except Employee.DoesNotExist:
        return Response({"detail": "Employee not found."}, status=status.HTTP_404_NOT_FOUND)

    # Update employee's fields from the request
    employee.department = request.data.get('department', employee.department)
    employee.position = request.data.get('position', employee.position)
    employee.date_of_joining = request.data.get('date_of_joining', employee.date_of_joining)
    employee.save()

    serializer = EmployeeSerializer(employee)
    return Response({"detail": "Employee updated successfully.", "employee": serializer.data}, status=status.HTTP_200_OK)


# Delete an employee (Admin only)
@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_employee(request, employee_id):
    if not request.user.is_staff:
        return Response({"detail": "Permission Denied. Admins only."}, status=status.HTTP_403_FORBIDDEN)

    try:
        employee = Employee.objects.get(id=employee_id)
        employee.delete()
        return Response({"detail": "Employee deleted successfully."}, status=status.HTTP_204_NO_CONTENT)
    except Employee.DoesNotExist:
        return Response({"detail": "Employee not found."}, status=status.HTTP_404_NOT_FOUND)
      
