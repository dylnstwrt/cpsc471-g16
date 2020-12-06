"""
    docstring
"""
from django.db import models

# Create your models here.


class Employee(models.Model):
    """
    docstring
    """
    emp_id = models.IntegerField(max_length=8)
    wage = models.FloatField()
    join_date = models.DateField(auto_now=False, auto_now_add=True)
    employed = models.BooleanField()

    class Meta:
        app_label = 'api'
        abstract = True

    def __str__(self):
        return str(self.emp_id)


class Manager(Employee):
    """
    docstring
    """
    man_id = models.IntegerField(max_length=8)
    man_type = models.CharField(max_length=5)

    class Meta:
        app_label = 'api'
        abstract = True

    def __str__(self):
        return str(self.man_id)


class Administrator(Manager):
    """
    docstring
    """
    admin_id = models.IntegerField(max_length=8)

    class Meta:
        app_label = 'api'

    def __str__(self):
        return str(self.admin_id)

class Equipment(models.Model):
    """
    Docstring
    """
    eq_id = models.IntegerField()
    model = models.CharField( max_length=50)
    date_aquired = models.DateField( auto_now=False, auto_now_add=False)
    eq_type = models.CharField(max_length=50)

class Fixture(Equipment):
    """
    docstring here
    """
    description = models.CharField(max_length=50)

    class Meta:
        app_id = 'api'

    def __str__(self):
        return str(self.eq_id)

class Till(Equipment):
    """
    Docstring
    """
    serial_no = models.IntegerField(max_length=8)
    operating_system = models.CharField(max_length=50)

    class Meta:
        app_id = 'api'

    def __str__(self):
        return str(self.serial_no)

class Transaction(models.Model):
    """
    docstring
    """
    tid = models.IntegerField(max_length=8)
    eid = models.ForeignKey(Employee, on_delete=models.CASCADE)
    payment_method = models.CharField(max_length=50)
    customer_email = models.CharField(max_length=50)
    subtotal = models.FloatField()
    sales_tax = models.FloatField()
    total = models.FloatField()
    serial_no = models.ForeignKey(Till, on_delete=models.SET_NULL)

    class Meta:
        app_label = 'api'
        abstract = True

    def __str__(self):
        return str(self.tid)


class Sale(Transaction):
    """
    docstring
    """
    profit = models.FloatField()

    class Meta:
        app_label = 'api'


class Return(Transaction):
    """
    docstring
    """
    original_tid = models.ForeignKey(Transaction, on_delete=models.SET_NULL)
    reason = models.CharField(max_length=50)

    class Meta:
        app_label = 'api'


class Special(Transaction):
    """
    docstring
    """
    models.ForeignKey(Manager, on_delete=models.SET_NULL)


class Brand(models.Model):
    """
    docstring
    """
    b_id = models.IntegerField(max_length=8)
    name = models.CharField(max_length=50)
    contact_num = models.IntegerField(max_length=12)

    class Meta:
        app_label = 'api'

    def __str__(self):
        return str(self.name)


class Distributor(models.Model):
    """
    docstring
    """
    dist_id = models.IntegerField(max_length=8)
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    contact_num = models.IntegerField(max_length=12)

    class Meta:
        app_id = 'api'

    def __str__(self):
        return str(self.name)

class Coupon(models.Model):
    """
    docstring
    """
    class DiscountTypes(models.TextChoices):
        FLAT = 'F', ('Flat')
        PERCENT = 'P', ('Percent')

    c_code = models.IntegerField(max_length=8)
    discount_type = models.CharField(
        max_length=1,
        choices=DiscountTypes.choices,
        default=DiscountTypes.FLAT
    )
    valid_before = models.DateField(auto_now=False, auto_now_add=False)
    amount = models.IntegerField()

    class Meta:
        app_id = 'api'

class IncidentReport(models.Model):
    """
    docstring
    """
    eid = models.ForeignKey(Employee, on_delete=models.SET_NULL)
    man_id = models.ForeignKey(Manager, on_delete=models.SET_NULL)
    action_taken = models.CharField(max_length=50)
    incident_date = models.DateField()
    filing_date = models.DateField(auto_now=False, auto_now_add=True)
    description = models.CharField(max_length=50)

    class Meta:
        app_id = 'api'
