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


class EquipmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Equipment
        fields = '__all__'


class FixtureSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Fixture
        fields = '__all__'


class  TillSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Till
        fields = '__all__'


class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Transaction
        fields = '__all__'

        
class SaleSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Sale
        fields = '__all__'

        
class ReturnSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Return
        fields = '__all__'

        
class SpecialSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Special
        fields = '__all__'

        
class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Brand
        fields = '__all__'

        
class DistributorSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Distributor
        fields = '__all__'

        
class CouponSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Coupon
        fields = '__all__'

        
class  IncidentReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.IncidentReport
        fields = '__all__'

        
class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Item
        fields = '__all__'

        
class ClothingSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Clothing
        fields = '__all__'

        
class BottomSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Bottom
        fields = '__all__'

        
class TopSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Top
        fields = '__all__'

        
class AccessorySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Accessory
        fields = '__all__'

class BasketSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Basket
        fields = '__all__'

class FinancialSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Financial
        fields = '__all__'

class DiscountSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Discount
        fields = '__all__'

class DistributeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Distributes
        fields = '__all__'