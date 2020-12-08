"""
    TODO:
        
"""
from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.forms.models import model_to_dict
from django.core import serializers


# Create your models here.
#

class Employee(models.Model):
    """
    docstring
    """
    emp_id = models.IntegerField(unique=True)
    wage = models.FloatField()
    join_date = models.DateField(auto_now=False, auto_now_add=True)
    employed = models.BooleanField()

    class Meta:
        app_label = 'api'
        #abstract = True

    def __str__(self):
        return str(self.emp_id)

################################################

class Manager(Employee):
    """
    docstring
    """
    man_id = models.IntegerField(unique=True)
    man_type = models.CharField(max_length=5)

    class Meta:
        app_label = 'api'
        ##abstract = True

    def __str__(self):
        return str(self.man_id)

################################################

class Administrator(Manager):
    """
    docstring
    """
    admin_id = models.IntegerField(unique=True)

    class Meta:
        app_label = 'api'

    def __str__(self):
        return str(self.admin_id)

################################################

class Equipment(models.Model):
    """
    Docstring
    """
    eq_id = models.IntegerField(unique=True)
    model = models.CharField(max_length=50)
    date_aquired = models.DateField(auto_now=False, auto_now_add=False)
    eq_type = models.CharField(max_length=50)

    class Meta:
        app_label = 'api'
        #abstract = True

    def __str__(self):
        return str(self.eq_id)

################################################

class Fixture(Equipment):
    """
    docstring here
    """
    description = models.CharField(max_length=50)

    class Meta:
        app_label = 'api'

################################################

class Till(Equipment):
    """
    Docstring
    """
    serial_no = models.IntegerField(unique=True)
    operating_system = models.CharField(max_length=50)

    class Meta:
        app_label = 'api'

    def __str__(self):
        return str(self.serial_no)

################################################

class Transaction(models.Model):
    """
    docstring
    """
    tid = models.IntegerField(unique=True)
    eid = models.ForeignKey(Employee, on_delete=models.SET_NULL, null=True)
    payment_method = models.CharField(max_length=50)
    customer_email = models.CharField(max_length=50)
    subtotal = models.FloatField(
        default=0.00
    )
    sales_tax = models.FloatField(
        default=0.00
    )
    total = models.FloatField(
        default=0.00
    )
    serial_no = models.ForeignKey(Till, on_delete=models.SET_NULL, null=True)
    completed = models.BooleanField(
        default=False
    )
    message = models.CharField(
        max_length=50,
        editable=False,
        default="",
        )

    class Meta:
        app_label = 'api'
        #abstract = True

    def __str__(self):
        return str(self.tid)



################################################

class Sale(Transaction):
    """
    docstring
    """
    profit = models.FloatField(
        default=0.00
    )

    class Meta:
        app_label = 'api'

################################################

class Return(Transaction):
    """
    docstring
    """
    original_tid = models.ForeignKey(Transaction, on_delete=models.SET_NULL, related_name="sale_tid", null=True)
    reason = models.CharField(max_length=50)

    class Meta:
        app_label = 'api'

################################################

class Special(Transaction):
    """
    docstring
    """
    models.ForeignKey(Manager, on_delete=models.SET_NULL, null=True)

    class Meta:
        app_label = 'api'

################################################

class Brand(models.Model):
    """
    docstring
    """
    b_id = models.IntegerField(unique=True)
    name = models.CharField(max_length=50)
    contact_num = models.IntegerField()

    class Meta:
        app_label = 'api'

    def __str__(self):
        return str(self.name)

################################################

class Distributor(models.Model):
    """
    docstring
    """
    dist_id = models.IntegerField(unique=True)
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    contact_num = models.IntegerField()

    class Meta:
        app_label = 'api'

    def __str__(self):
        return str(self.name)

################################################

class Coupon(models.Model):
    """
    docstring
    """
    class DiscountTypes(models.TextChoices):
        FLAT = 'F', ('Flat')
        PERCENT = 'P', ('Percent')

    c_code = models.IntegerField(unique=True)
    discount_type = models.CharField(
        max_length=1,
        choices=DiscountTypes.choices,
        default=DiscountTypes.FLAT
    )
    valid_before = models.DateField(auto_now=False, auto_now_add=False)
    amount = models.IntegerField()

    class Meta:
        app_label = 'api'

    def __str__(self):
        return str(self.c_code)

################################################

class IncidentReport(models.Model):
    """
    docstring
    """
    eid = models.ForeignKey(Employee, on_delete=models.SET_NULL, related_name="employee_id", null=True)
    man_id = models.ForeignKey(Manager, on_delete=models.SET_NULL, related_name="manager_id", null=True)
    action_taken = models.CharField(max_length=50)
    incident_date = models.DateField()
    filing_date = models.DateField(auto_now=False, auto_now_add=True)
    description = models.CharField(max_length=50)

    class Meta:
        app_label = 'api'

    def __str__(self):
        return str(self.description)

################################################

class Item(models.Model):
    """
    docstring
    """
    upc = models.IntegerField(unique=True)
    name = models.CharField(max_length=50)
    colour = models.CharField(max_length=50)
    description = models.CharField(max_length=50)
    stock_quantity = models.IntegerField()
    sales_price = models.FloatField()
    unit_price = models.FloatField()
    b_id = models.ForeignKey(Brand, on_delete=models.SET_NULL, null=True)

    class Meta:
        app_label = 'api'
        #abstract = True

    def __str__(self):
        return str(self.name)

################################################

class Clothing(Item):
    """
    docstring
    """
    material = models.CharField(max_length=50)
    cl_type = models.CharField(max_length=50)

    class Meta:
        app_label = 'api'
        #abstract = True

################################################

class Bottom(Clothing):
    """
    docstring
    """
    waist = models.IntegerField()
    length = models.IntegerField()

    class Meta:
        app_label = 'api'

################################################

class Top(Clothing):
    """
    docstring
    """
    class SizeChoices(models.TextChoices):
        XSMALL = 'XS', ('Extra-Small')
        SMALL = 'S', ('Small')
        MEDIUM = 'M', ('Medium')
        LARGE = 'L', ('Large')
        XLARGE = 'XL', ('Extra-Large')

    size = models.CharField(
        max_length=2,
        choices=SizeChoices.choices,
        default=SizeChoices.MEDIUM
    )

    class Meta:
        app_label = 'api'

################################################

class Accessory(Item):
    """
    docstring
    """
    ac_type = models.CharField(max_length=50)

    class Meta:
        app_label = 'api'

################################################

class Basket(models.Model):
    """
    docstring later
    """
    tid = models.ForeignKey(Transaction, on_delete=models.CASCADE)
    #upc = models.ForeignKey(Item, on_delete=models.CASCADE)
    basket_item = models.ManyToManyField(Item)

    class Meta:
        app_label = 'api'

class Distributes(models.Model):
    """

    """
    dist_id = models.ForeignKey(Distributor, on_delete=models.SET_NULL, null=True)
    item_upc = models.ForeignKey(Item, on_delete=models.SET_NULL, null=True)
    

    class Meta:
        app_label = 'api'

class Discounts:
    tid = models.ForeignKey(Transaction, on_delete=models.CASCADE)

    class Meta:
        app_label = 'api'
"""
docstring: 
TODO: do stuff to financial view if possible
"""
@receiver(pre_save, sender=Sale)
def update_item_decrement(sender, instance,  **kwargs):
    if instance.completed:
        print("Calculating Subtotal: ")
        basket_instances = Basket.objects.filter(tid = instance.id)
        subtotal = 0
        profit = 0
        warnings = ""
        for basket in basket_instances:
            item_obj = basket.basket_item.all().first()
            if item_obj is not None:
                subtotal += item_obj.sales_price
                profit += item_obj.sales_price - item_obj.unit_price
                item_obj.stock_quantity -= 1
                if item_obj.stock_quantity < 2: # set threshold here
                    warnings += " LowStock:{item_obj.name}_{item_obj.upc}"
        instance.subtotal = subtotal
        instance.sales_tax = .05 * subtotal
        instance.total = subtotal + instance.sales_tax
        instance.message = "Completed_Sale"+warnings
        

'''
haven't tested this yet
'''
@receiver(pre_save, sender=Return)
def update_item_increment(sender, instance,  **kwargs):
    if instance.completed:
        print("Calculating Subtotal: ")
        basket_instances = Basket.objects.filter(tid = instance.id)
        subtotal = 0
        profit = 0
        for basket in basket_instances:
            item_obj = basket.basket_item.all().first()
            if item_obj is not None:
                subtotal -= item_obj.sales_price
                profit -= item_obj.sales_price - item_obj.unit_price
                item_obj.stock_quantity += 1
        instance.subtotal = subtotal
        instance.sales_tax = .05 * subtotal
        instance.total = subtotal + instance.sales_tax
