from django.urls import path, include
from . import views

urlpatterns = [
    path('employees', views.EmployeeList.as_view()),
    path('managers', views.ManagerList.as_view()),
    path('administrators', views.AdministratorList.as_view()),

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
    path('accessorys', views.AccessoryList.as_view()),
    path('baskets', views.BasketList.as_view())
]

