from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status, viewsets
from . import serializers
from . import models

class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = models.Employee.objects.all()
    serializer_class = serializers.EmployeeSerializer

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

class EmployeeSingle(APIView):
    def get(self, request, emp_id, format=None):
        employee = models.Employee.objects.get (emp_id=emp_id)
        serializer = serializers.EmployeeSerializer(employee)
        return Response (serializer.data)

################################################

class ManagerViewSet(viewsets.ModelViewSet):
    queryset = models.Manager.objects.all()
    serializer_class = serializers.ManagerSerializer

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

class ManagerSingle(APIView):
    def get(self, request, man_id, format=None):
        manager = models.Manager.objects.get (man_id=man_id)
        serializer = serializers.ManagerSerializer(manager)
        return Response (serializer.data)

################################################
class AdministratorViewSet(viewsets.ModelViewSet):
    queryset = models.Administrator.objects.all()
    serializer_class = serializers.AdministratorSerializer

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

class AdministratorSingle(APIView):
    def get(self, request, admin_id, format=None):
        admin = models.Administrator.objects.get (admin_id = admin_id)
        serializer = serializers.AdministratorSerializer(admin)
        return Response (serializer.data)

################################################
class EquipmentViewSet(viewsets.ModelViewSet):
    queryset = models.Equipment.objects.all()
    serializer_class = serializers.EquipmentSerializer

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
class TillViewSet(viewsets.ModelViewSet):
    queryset = models.Till.objects.all()
    serializer_class = serializers.TillSerializer

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
class FixtureViewSet(viewsets.ModelViewSet):
    queryset = models.Fixture.objects.all()
    serializer_class = serializers.FixtureSerializer

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
class TransactionViewSet(viewsets.ModelViewSet):
    queryset = models.Transaction.objects.all()
    serializer_class = serializers.TransactionSerializer

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
class SalesViewSet(viewsets.ModelViewSet):
    queryset = models.Sale.objects.all()
    serializer_class = serializers.SaleSerializer

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
class ReturnViewSet(viewsets.ModelViewSet):
    queryset = models.Return.objects.all()
    serializer_class = serializers.ReturnSerializer

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
class SpecialViewSet(viewsets.ModelViewSet):
    queryset = models.Special.objects.all()
    serializer_class = serializers.SpecialSerializer

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
class BrandViewSet(viewsets.ModelViewSet):
    queryset = models.Brand.objects.all()
    serializer_class = serializers.BrandSerializer

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
class DistributorViewSet(viewsets.ModelViewSet):
    queryset = models.Distributor.objects.all()
    serializer_class = serializers.DistributorSerializer

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
class CouponViewSet(viewsets.ModelViewSet):
    queryset = models.Coupon.objects.all()
    serializer_class = serializers.CouponSerializer

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
class IncidentReportViewSet(viewsets.ModelViewSet):
    queryset = models.IncidentReport.objects.all()
    serializer_class = serializers.IncidentReportSerializer

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
class ItemViewSet(viewsets.ModelViewSet):
    queryset = models.Item.objects.all()
    serializer_class = serializers.ItemSerializer

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
class ClothingViewSet(viewsets.ModelViewSet):
    queryset = models.Clothing.objects.all()
    serializer_class = serializers.ClothingSerializer


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
class BottomViewSet(viewsets.ModelViewSet):
    queryset = models.Bottom.objects.all()
    serializer_class = serializers.BottomSerializer

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
class TopViewSet(viewsets.ModelViewSet):
    queryset = models.Top.objects.all()
    serializer_class = serializers.TopSerializer

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
class AcessoryViewSet(viewsets.ModelViewSet):
    queryset = models.Accessory.objects.all()
    serializer_class = serializers.AccessorySerializer

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
class BasketViewSet(viewsets.ModelViewSet):
    queryset = models.Basket.objects.all()
    serializer_class = serializers.BasketSerializer

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

class FinancialViewSet(viewsets.ModelViewSet):
    queryset = models.Financial.objects.all().order_by('timestamp')
    serializer_class = serializers.FinancialSerializer

class DiscountViewSet(viewsets.ModelViewSet):
    queryset = models.Discount.objects.all()
    serializer_class = serializers.DiscountSerializer

class DistributeViewSet(viewsets.ModelViewSet):
    queryset = models.Distributes.objects.all()
    serializer_class = serializers.DistributeSerializer