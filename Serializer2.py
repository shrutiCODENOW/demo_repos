from rest_framework import serializers
from .models import User, Department, Employee, Attendance, LeaveRequest


# User Serializer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "first_name", "last_name", "email", "is_admin", "is_employee"]


# Department Serializer
class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = ["id", "name", "created_at"]


# Employee Serializer
class EmployeeSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    department = DepartmentSerializer(read_only=True)

    class Meta:
        model = Employee
        fields = ["id", "user", "department", "hire_date", "address", "phone_number"]


# Attendance Serializer
class AttendanceSerializer(serializers.ModelSerializer):
    employee = serializers.StringRelatedField()  # Displays employee name instead of ID

    class Meta:
        model = Attendance
        fields = ["id", "employee", "date", "status"]


# Leave Request Serializer
class LeaveRequestSerializer(serializers.ModelSerializer):
    employee = serializers.StringRelatedField(read_only=True)  # Displays employee name instead of ID

    class Meta:
        model = LeaveRequest
        fields = ["id", "employee", "start_date", "end_date", "reason", "status", "requested_at"]
        read_only_fields = ["status", "requested_at"]  # Status is managed by the admin
