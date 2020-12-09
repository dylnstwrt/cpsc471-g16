from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'employee', views.EmployeeViewSet)
router.register(r'manager', views.ManagerViewSet)
router.register(r'administrator', views.AdministratorViewSet)
router.register(r'equipment', views.EquipmentViewSet)
router.register(r'till', views.TillViewSet)
router.register(r'fixture', views.FixtureViewSet)
router.register(r'transaction', views.TransactionViewSet)
router.register(r'sale', views.SalesViewSet)
router.register(r'return', views.ReturnViewSet)
router.register(r'special', views.SpecialViewSet)
router.register(r'brand', views.BrandViewSet)
router.register(r'distributor', views.DistributorViewSet)
router.register(r'coupon', views.CouponViewSet)
router.register(r'incident_report', views.IncidentReportViewSet)
router.register(r'item', views.ItemViewSet)
router.register(r'clothing', views.ClothingViewSet)
router.register(r'bottom', views.BottomViewSet)
router.register(r'top', views.TopViewSet)
router.register(r'accessory', views.AcessoryViewSet)
router.register(r'basket', views.BasketViewSet)
router.register(r'financial', views.FinancialViewSet)
router.register(r'discount', views.DiscountViewSet)
router.register(r'distribute', views.DistributeViewSet)


urlpatterns = [
    path('',include(router.urls)),
]
