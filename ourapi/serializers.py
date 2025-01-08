from rest_framework import serializers
from ourapi.models import Company , Employee



class CompanySerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        Company_id = serializers.ReadOnlyField()
        model = Company
        fields = "__all__"
        
class EmployeeSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        Employee_id = serializers.ReadOnlyField()
        model = Employee
        fields = "__all__"        