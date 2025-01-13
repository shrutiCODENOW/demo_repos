# employees/models.py

from django.db import models

class Department(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Employee(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    hire_date = models.DateField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Attendance(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    date = models.DateField()
    status_choices = [
        ('P', 'Present'),
        ('A', 'Absent'),
        ('L', 'Leave'),
    ]
    status = models.CharField(max_length=1, choices=status_choices)

    def __str__(self):
        return f"{self.employee} - {self.date} - {self.get_status_display()}"


class LeaveRequest(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    reason = models.TextField()
    status_choices = [
        ('P', 'Pending'),
        ('A', 'Approved'),
        ('R', 'Rejected'),
    ]
    status = models.CharField(max_length=1, choices=status_choices, default='P')

    def __str__(self):
        return f"Leave Request by {self.employee} ({self.get_status_display()})"
      
