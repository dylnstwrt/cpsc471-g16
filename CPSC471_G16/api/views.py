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

################################################

class ManagerList(APIView):
    def get(self, request, format=None):
        managers = models.Manager.objects.all()
        serializer = serializers.EmployeeSerializer(managers, many=True)
        return Response (serializer.data)

    def post(self, request, format=None):
        serializer = serializers.ManagerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response (serializer.data, status=status.HTTP_201_CREATED)
        return Response (serializer.errors, status=status.HTTP_400_BAD_REQUEST)

################################################

class AdministratorList(APIView):
    def get(self, request, format=None):
        administrators = models.Administrator.objects.all()
        serializer = serializers.AdministratorSerializer(administrators, many=True)
        return Response (serializer.data)
    def post(self, request, format=None):
        serializer = serializers.AdministratorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response (serializer.data, status=status.HTTP_201_CREATED)
        return Response (serializer.errors, status=status.HTTP_400_BAD_REQUEST)

################################################

class EquipmentList(APIView):
    def get(self, request, format=None):
        equipment = models.Equipment.objects.all()
        serializer = serializers.EquipmentSerializer(equipment, many=True)
        return Response (serializer.data)

    def post(self, request, format=None):
        serializer = serializers. EquipmentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response (serializer.data, status=status.HTTP_201_CREATED)
        return Response (serializer.errors, status=status.HTTP_400_BAD_REQUEST)

################################################

class TillList(APIView):
    def get(self, request, format=None):
        tills = models.Till.objects.all()
        serializer = serializers.TillSerializer(tills, many=True)
        return Response (serializer.data)

    def post(self, request, format=None):
        serializer = serializers.TillSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response (serializer.data, status=status.HTTP_201_CREATED)
        return Response (serializer.errors, status=status.HTTP_400_BAD_REQUEST)

################################################

class FixtureList(APIView):
    def get(self, request, format=None):
        fixtures = models.Fixture.objects.all()
        serializer = serializers.FixtureSerializer(fixtures, many=True)
        return Response (serializer.data)

    def post(self, request, format=None):
        serializer = serializers.FixtureSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response (serializer.data, status=status.HTTP_201_CREATED)
        return Response (serializer.errors, status=status.HTTP_400_BAD_REQUEST)

################################################

class TransactionList(APIView):
    def get(self, request, format=None):
        transactions = models.Employee.objects.all()
        serializer = serializers.TransactionSerializer(transactions, many=True)
        return Response (serializer.data)

    def post(self, request, format=None):
        serializer = serializers.TransactionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response (serializer.data, status=status.HTTP_201_CREATED)
        return Response (serializer.errors, status=status.HTTP_400_BAD_REQUEST)

################################################

class SaleList(APIView):
    def get(self, request, format=None):
        sales = models.Sale.objects.all()
        serializer = serializers.SaleSerializer(sales, many=True)
        return Response (serializer.data)

    def post(self, request, format=None):
        serializer = serializers.SaleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response (serializer.data, status=status.HTTP_201_CREATED)
        return Response (serializer.errors, status=status.HTTP_400_BAD_REQUEST)

################################################

class ReturnList(APIView):
    def get(self, request, format=None):
        returns = models.Return.objects.all()
        serializer = serializers.ReturnSerializer(returns, many=True)
        return Response (serializer.data)

    def post(self, request, format=None):
        serializer = serializers.ReturnSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response (serializer.data, status=status.HTTP_201_CREATED)
        return Response (serializer.errors, status=status.HTTP_400_BAD_REQUEST)

################################################

class SpecialList(APIView):
    def get(self, request, format=None):
        specials = models.Special.objects.all()
        serializer = serializers.SpecialSerializer(specials, many=True)
        return Response (serializer.data)

    def post(self, request, format=None):
        serializer = serializers.SpecialSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response (serializer.data, status=status.HTTP_201_CREATED)
        return Response (serializer.errors, status=status.HTTP_400_BAD_REQUEST)
################################################

class BrandList(APIView):
    def get(self, request, format=None):
        brands = models.Brand.objects.all()
        serializer = serializers.BrandSerializer(brands, many=True)
        return Response (serializer.data)

    def post(self, request, format=None):
        serializer = serializers.BrandSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response (serializer.data, status=status.HTTP_201_CREATED)
        return Response (serializer.errors, status=status.HTTP_400_BAD_REQUEST)

################################################

class DistributorList(APIView):
    def get(self, request, format=None):
        distributors = models.Distributor.objects.all()
        serializer = serializers.DistributorSerializer(distributors, many=True)
        return Response (serializer.data)

    def post(self, request, format=None):
        serializer = serializers.DistributorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response (serializer.data, status=status.HTTP_201_CREATED)
        return Response (serializer.errors, status=status.HTTP_400_BAD_REQUEST)

################################################

class CouponList(APIView):
    def get(self, request, format=None):
        coupons = models.Coupon.objects.all()
        serializer = serializers.CouponSerializer(coupons, many=True)
        return Response (serializer.data)

    def post(self, request, format=None):
        serializer = serializers.CouponSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response (serializer.data, status=status.HTTP_201_CREATED)
        return Response (serializer.errors, status=status.HTTP_400_BAD_REQUEST)

################################################

class IncidentReportList(APIView):
    def get(self, request, format=None):
        incidentReports = models.IncidentReport.objects.all()
        serializer = serializers.IncidentReportSerializer(incidentReports, many=True)
        return Response (serializer.data)

    def post(self, request, format=None):
        serializer = serializers.IncidentReportSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response (serializer.data, status=status.HTTP_201_CREATED)
        return Response (serializer.errors, status=status.HTTP_400_BAD_REQUEST)

################################################

class ItemList(APIView):
    def get(self, request, format=None):
        items = models.Item.objects.all()
        serializer = serializers.ItemSerializer(items, many=True)
        return Response (serializer.data)

    def post(self, request, format=None):
        serializer = serializers.ItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response (serializer.data, status=status.HTTP_201_CREATED)
        return Response (serializer.errors, status=status.HTTP_400_BAD_REQUEST)

################################################

class ClothingList(APIView):
    def get(self, request, format=None):
        clothing = models.Item.objects.all()
        serializer = serializers.ClothingSerializer(clothing, many=True)
        return Response (serializer.data)

    def post(self, request, format=None):
        serializer = serializers.ClothingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response (serializer.data, status=status.HTTP_201_CREATED)
        return Response (serializer.errors, status=status.HTTP_400_BAD_REQUEST)

################################################

class BottomList(APIView):
    def get(self, request, format=None):
        bottoms = models.Bottom.objects.all()
        serializer = serializers.BottomSerializer(bottoms, many=True)
        return Response (serializer.data)

    def post(self, request, format=None):
        serializer = serializers.BottomSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response (serializer.data, status=status.HTTP_201_CREATED)
        return Response (serializer.errors, status=status.HTTP_400_BAD_REQUEST)

################################################

class ItemList(APIView):
    def get(self, request, format=None):
        items = models.Item.objects.all()
        serializer = serializers.ItemSerializer(items, many=True)
        return Response (serializer.data)

    def post(self, request, format=None):
        serializer = serializers.ItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response (serializer.data, status=status.HTTP_201_CREATED)
        return Response (serializer.errors, status=status.HTTP_400_BAD_REQUEST)

################################################

class TopList(APIView):
    def get(self, request, format=None):
        tops = models.Top.objects.all()
        serializer = serializers.TopSerializer(tops, many=True)
        return Response (serializer.data)

    def post(self, request, format=None):
        serializer = serializers.TopSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response (serializer.data, status=status.HTTP_201_CREATED)
        return Response (serializer.errors, status=status.HTTP_400_BAD_REQUEST)

################################################

class AccessoryList(APIView):
    def get(self, request, format=None):
        accessorys = models.Accessory.objects.all()
        serializer = serializers.AccessorySerializer(accessorys, many=True)
        return Response (serializer.data)

    def post(self, request, format=None):
        serializer = serializers.AccessorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response (serializer.data, status=status.HTTP_201_CREATED)
        return Response (serializer.errors, status=status.HTTP_400_BAD_REQUEST)

################################################

class BasketList(APIView):
    def get(self, request, format=None):
        baskets = models.Basket.objects.all()
        serializer = serializers.BasketSerializer(baskets, many=True)
        return Response (serializer.data)

    def post(self, request, format=None):
        serializer = serializers.BasketSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response (serializer.data, status=status.HTTP_201_CREATED)
        return Response (serializer.errors, status=status.HTTP_400_BAD_REQUEST)

