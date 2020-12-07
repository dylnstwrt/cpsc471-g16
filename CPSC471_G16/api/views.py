from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from . import serializers
from . import models

class EmployeeList(APIView):
    def get(self, request, format=None):
        employees = models.Employee.objects.all()
        serializer = serializers.EmployeeSerializer(employees, many=True)
        return Response (serializer.data)

    def post(self, request, format=None):
        serializer = serializers.EmployeeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response (serializer.data, status=status.HTTP_201_CREATED)
        return Response (serializer.errors, status=status.HTTP_400_BAD_REQUEST)