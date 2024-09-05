from django.urls import path
from customers import views
from product import auth
from customers.views import ExportData
urlpatterns = [
    path('', views.CustomerListView.as_view(), name='customer_list'),
    path('detail/<int:customer_id>/', views.CustomerDetailView.as_view(), name='customer_detail'),
    path('create/', views.CustomerCreateView.as_view(), name='customer_create'),
    path('edit/<int:customer_id>/', views.CustomerUpdateView.as_view(), name='customer_update'),
    path('delete/<int:customer_id>/', views.CustomerDeleteView.as_view(), name='customer_delete'),

    path('login-page/', auth.LoginPage.as_view(), name='login_page'),
    path('register-page/', auth.RegisterPage.as_view(), name='register_page'),
    path('logout_page/', auth.logout_page, name='logout_page'),
    path('export/', ExportData.as_view(), name='export_data'),
]
