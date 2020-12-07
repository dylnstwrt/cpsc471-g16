from rest_framework import serializers
from . import models


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Employee
        fields = '__all__'

class ManagerSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Manager
        fields = '__all__'

class AdministratorSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Administrator
        fields = '__all__'