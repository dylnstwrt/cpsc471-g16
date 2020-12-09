from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'employee_pretty', views.EmployeeViewSet)
router.register(r'manager_pretty', views.ManagerViewSet)
router.register(r'administrator_pretty', views.AdministratorViewSet)
router.register(r'equipment_pretty', views.EquipmentViewSet)
router.register(r'till_pretty', views.TillViewSet)
router.register(r'fixture_pretty', views.FixtureViewSet)
router.register(r'transaction_pretty', views.TransactionViewSet)
router.register(r'sale_pretty', views.SalesViewSet)
router.register(r'return_pretty', views.ReturnViewSet)
router.register(r'special_pretty', views.SpecialViewSet)
router.register(r'brand_pretty', views.BrandViewSet)
router.register(r'distributor_pretty', views.DistributorViewSet)
router.register(r'coupon_pretty', views.CouponViewSet)
router.register(r'incident_report_pretty', views.IncidentReportViewSet)
router.register(r'item_pretty', views.ItemViewSet)
router.register(r'clothing_pretty', views.ClothingViewSet)
router.register(r'bottom_pretty', views.BottomViewSet)
router.register(r'top_pretty', views.TopViewSet)
router.register(r'accessory_pretty', views.AcessoryViewSet)
router.register(r'basket_pretty', views.BasketViewSet)
router.register(r'financial_pretty', views.FinancialViewSet)
#router.register(r'discount_pretty', views.DiscountViewSet)
#router.register(r'distribute_pretty', views.Distributes)


urlpatterns = [
    path('',include(router.urls)),
    path('employees', views.EmployeeList.as_view()),
    path('employee/<int:emp_id>', views.EmployeeSingle.as_view()),
    path('managers', views.ManagerList.as_view()),
    path('manager/<int:man_id>', views.ManagerSingle.as_view()),
    path('administrators', views.AdministratorList.as_view()),
    path('administrators/<int:admin_id>', views.AdministratorSingle.as_view()),

    path('equipment', views.EquipmentList.as_view()),
    path('till', views.TillList.as_view()),
    path('fixtures', views.FixtureList.as_view()),
    path('transactions', views.TransactionList.as_view()),
    path('sales', views.SaleList.as_view()),
    path('returns', views.ReturnList.as_view()),
    path('specials', views.SpecialList.as_view()),
    path('brands', views.BrandList.as_view()),
    path('distributors', views.DistributorList.as_view()),
    path('coupons', views.CouponList.as_view()),
    path('incidentReports', views.IncidentReportList.as_view()),
    path('items', views.ItemList.as_view()),
    path('clothing', views.ClothingList.as_view()),
    path('bottoms', views.BottomList.as_view()),
    path('tops', views.TopList.as_view()),
    path('accessories', views.AccessoryList.as_view()),
    path('baskets', views.BasketList.as_view())
]
