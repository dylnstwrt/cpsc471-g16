'''
CPSC471 - Group 16
'''
from datetime import datetime

from django.core.signals import request_finished
from django.db import connection, models
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver

# Create your models here.
#


class Employee(models.Model):
    """
    Employee Model
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
    Manager Model
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
    Administrator Model
    """
    admin_id = models.IntegerField(unique=True)

    class Meta:
        app_label = 'api'

    def __str__(self):
        return str(self.admin_id)

################################################


class Equipment(models.Model):
    """
    Equipment Model
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
    Fixture Model
    """
    description = models.CharField(max_length=50)

    class Meta:
        app_label = 'api'

################################################


class Till(Equipment):
    """
    Till Model
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
    Transaction Model
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
    Sale Model
    """
    profit = models.FloatField(
        default=0.00
    )

    class Meta:
        app_label = 'api'

################################################


class Return(Transaction):
    """
    Return Model
    """
    original_tid = models.ForeignKey(
        Transaction, on_delete=models.SET_NULL, related_name="sale_tid", null=True)
    reason = models.CharField(max_length=50)

    class Meta:
        app_label = 'api'

################################################


class Special(Transaction):
    """
    Special Model
    """
    models.ForeignKey(Manager, on_delete=models.SET_NULL, null=True)

    class Meta:
        app_label = 'api'

################################################


class Brand(models.Model):
    """
    Brand Model
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
    Distributor Model
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
    Coupon Model
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
    Incident Report Model
    """
    eid = models.ForeignKey(
        Employee, on_delete=models.SET_NULL, related_name="employee_id", null=True)
    man_id = models.ForeignKey(
        Manager, on_delete=models.SET_NULL, related_name="manager_id", null=True)
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
    Item Model
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
    Clothing Model
    """
    material = models.CharField(max_length=50)
    cl_type = models.CharField(max_length=50)

    class Meta:
        app_label = 'api'
        #abstract = True

################################################


class Bottom(Clothing):
    """
    Bottom Model
    """
    waist = models.IntegerField()
    length = models.IntegerField()

    class Meta:
        app_label = 'api'

################################################


class Top(Clothing):
    """
    Top Model
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
    Accessory Model
    """
    ac_type = models.CharField(max_length=50)

    class Meta:
        app_label = 'api'

################################################


class Basket(models.Model):
    """
    Basket Instance Model
    """
    tid = models.ForeignKey(Transaction, on_delete=models.CASCADE)
    #upc = models.ForeignKey(Item, on_delete=models.CASCADE)
    basket_item = models.ManyToManyField(Item)

    class Meta:
        app_label = 'api'


class Distributes(models.Model):
    """
    Distributes Instance Model
    """
    # change to manytomany
    dist_id = models.ManyToManyField(Distributor)
    item_upc = models.ForeignKey(Item, on_delete=models.CASCADE)

    class Meta:
        app_label = 'api'


class Discount(models.Model):
    '''
    Discounts Instance Model
    '''
    tid = models.ForeignKey(Transaction, on_delete=models.CASCADE)
    c_code = models.ManyToManyField(Coupon)
    #objects = models.Manager()

    class Meta:
        app_label = 'api'


class Financial(models.Model):
    '''
    Financial Information Instance Model
    '''
    timestamp = models.DateTimeField(auto_now_add=True)
    revenue = models.FloatField()
    sales_tax = models.FloatField()
    #inventory_cost = models.FloatField()
    profit = models.FloatField()

    class Meta:
        app_label = 'api'


@receiver(pre_save, sender=Sale)
def complete_sale(sender, instance,  **kwargs):
    '''
    Complete_Sale: updates financial, transaction, and item instance when transaction is complete.
    Decrements item count, and increments total revenue, profit, and tax.
    '''
    if instance.completed:
        print("Calculating Subtotal: ")
        basket_instances = Basket.objects.filter(tid=instance.id)
        subtotal = 0
        profit = 0
        warnings = ""
        for basket in basket_instances:
            item_obj = basket.basket_item.all().first()
            if item_obj is not None:
                subtotal += item_obj.sales_price
                profit += item_obj.sales_price - item_obj.unit_price
                item_obj.stock_quantity -= 1
                if item_obj.stock_quantity < 5 and item_obj.stock_quantity > 0:  # set threshold here
                    warnings += " LowStock:" + \
                        item_obj.name+"_"+str(item_obj.upc)
                elif item_obj.stock_quantity < 0:
                    warnings += " OverSold:" + \
                        item_obj.name+"_"+str(item_obj.upc)
                item_obj.save()

        instance.subtotal = subtotal
        instance.sales_tax = .05 * subtotal
        instance.total = subtotal + instance.sales_tax
        instance.profit = profit
        instance.message = "Completed_Sale"+warnings


@receiver(pre_save, sender=Special)
def complete_special(sender, instance,  **kwargs):
    '''
    Complete_Special: updates financial, transaction, and item instance when transaction is complete.
    Decrements item count, and increments total revenue, profit, and tax.
    '''
    if instance.completed:
        if instance.completed:
            print("Calculating Subtotal: ")
            basket_instances = Basket.objects.filter(tid=instance.id)
            subtotal = 0
            profit = 0
            warnings = ""
            for basket in basket_instances:
                item_obj = basket.basket_item.all().first()
                if item_obj is not None:
                    subtotal += item_obj.sales_price
                    profit += item_obj.sales_price - item_obj.unit_price
                    item_obj.stock_quantity -= 1
                    if item_obj.stock_quantity < 5 and item_obj.stock_quantity > 0:  # set threshold here
                        warnings += " LowStock:" + \
                            item_obj.name+"_"+str(item_obj.upc)
                    elif item_obj.stock_quantity < 0:
                        warnings += " OverSold:" + \
                            item_obj.name+"_"+str(item_obj.upc)
                    item_obj.save()

            instance.subtotal = subtotal
            instance.sales_tax = .05 * subtotal
            instance.total = subtotal + instance.sales_tax
            instance.message = "Completed_Sale"+warnings


@receiver(pre_save, sender=Return)
def complete_return(sender, instance,  **kwargs):
    '''
    Complete_Return: updates financial, transaction, and item instance when transaction is complete.
    Increments item count and decrements total revenue, profit, and tax.
    '''
    if instance.completed:

        original_sale = Sale.objects.filter(
            id=instance.original_tid.id).first()

        instance.subtotal = -original_sale.subtotal
        instance.sales_tax = -(.05 * original_sale.subtotal)
        instance.total = instance.subtotal + instance.sales_tax
        instance.message = "Completed_Return"

        basket_instances = Basket.objects.filter(tid=instance.original_tid.id)
        for basket in basket_instances:
            item_obj = basket.basket_item.all().first()
            if item_obj is not None:
                item_obj.stock_quantity += 1
                item_obj.save()


@receiver(post_save, sender=Sale)
def update_financials_sale(sender, instance, **kwargs):
    '''
    update_financials_sale: creates new timestamped instance of financial data when Sale is completed.
    '''
    total_rev = 0
    total_tax = 0
    total_profit = 0
    transactions = Sale.objects.all()
    for transaction in transactions:
        if transaction.completed:
            total_rev += transaction.total
            total_tax += transaction.sales_tax
            total_profit += transaction.profit
    financial_instance = Financial.objects.create(
        sales_tax=total_tax, profit=total_profit, revenue=total_rev)
    financial_instance.save()


@receiver(post_save, sender=Return)
def update_financials(sender, instance, **kwargs):
    '''
        update_financials_sale: creates new timestamped instance of financial data when Return is completed.
    '''
    total_rev = 0
    total_tax = 0
    total_profit = 0

    financial = Financial.objects.all().order_by('timestamp').last()
    original_sale = Sale.objects.filter(id=instance.original_tid.id).first()

    total_rev = financial.revenue - original_sale.subtotal
    total_tax = financial.sales_tax - original_sale.sales_tax
    total_profit = financial.profit - original_sale.profit

    financial_instance = Financial.objects.create(
        sales_tax=total_tax, profit=total_profit, revenue=total_rev)
    financial_instance.save()


@receiver(request_finished)
def print_query(**kwargs):
    '''
    print_query: prints the sql queries via terminal for each request made by a client.
    '''
    for query in connection.queries:
        query_str = datetime.now().strftime(
            "%d/%m/%Y %H:%M:%S") + "," + query['sql']
        print(query_str)
