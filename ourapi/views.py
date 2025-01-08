from django.shortcuts import render
from rest_framework import viewsets
from .serializers import CompanySerializers
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.exceptions import NotFound
from django.apps import apps

# Create your views here.

class Companyviewset(viewsets.ModelViewSet):
    queryset = apps.get_model('ourapi', 'Company').objects.all()  # Dynamically access the Company model
    serializer_class = CompanySerializers
    
    @action(detail=True, methods=['get'])
    def employees(self, request, pk=None):
        # Import EmployeeSerializers inside the method to avoid circular import
        from .serializers import EmployeeSerializers

        try:
            # Get the company instance
            company = self.get_object()  # Use the viewset's built-in method to get the company object
        except:
            raise NotFound(detail="Company not found.")

        # Dynamically access the Employee model using apps.get_model()
        Employee = apps.get_model('ourapi', 'Employee')
        
        # Filter employees associated with the company
        emps = Employee.objects.filter(company_id=company)

        # Serialize the employee data
        emps_serializer = EmployeeSerializers(emps, many=True, context={'request': request})
        
        # Return the response with serialized data
        return Response(emps_serializer.data)

class Employeeviewset(viewsets.ModelViewSet):
    # Import EmployeeSerializers here
    from .serializers import EmployeeSerializers
    
    queryset = apps.get_model('ourapi', 'Employee').objects.all()  # Dynamically access the Employee model
    serializer_class = EmployeeSerializers
