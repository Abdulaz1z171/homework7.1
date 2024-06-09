
from django.urls import path
from app.views import index,product_list,customer,customer_details,product_details,product_grid,detail,customer_add,edit_customer,delete_customer,to_login,logout,register

urlpatterns = [
    path('', index, name='index'),
    path('product-list/',product_list,name='product_list'),
    path('product-grid/',product_grid,name='product_grid'),
    path('product-details/',product_details,name='product_details'),
    path('customers/',customer, name = 'customer'),
    path('customer-details/<slug:slug>/',customer_details, name = 'customer_details'),
    path('detail/<int:pk>/', detail, name = 'detail'),
    path('customer-add/',customer_add, name = 'customer_add'),
    path('edit_customer/<int:pk>/', edit_customer, name = 'edit_customer'),
    path('delete_customer/<int:pk>/',delete_customer, name = 'delete_customer'),
    path('login/',to_login,name = 'login'),
    path('logout/',logout,name = 'logout'),
    path('register/',register,name = 'register')
]
