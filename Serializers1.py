# employees/serializers.py

from rest_framework import serializers
from .models import Employee, Attendance, LeaveRequest, Department


class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = ['id', 'name']


class EmployeeSerializer(serializers.ModelSerializer):
    department = DepartmentSerializer()

    class Meta:
        model = Employee
        fields = ['id', 'first_name', 'last_name', 'email', 'phone', 'department', 'hire_date']


class AttendanceSerializer(serializers.ModelSerializer):
    employee = EmployeeSerializer()

    class Meta:
        model = Attendance
        fields = ['id', 'employee', 'date', 'status']


class LeaveRequestSerializer(serializers.ModelSerializer):
    employee = EmployeeSerializer()

    class Meta:
        model = LeaveRequest
        fields = ['id', 'employee', 'start_date', 'end_date', 'reason', 'status']
      
