from django.urls import path
from customers import views
from customers import auth
urlpatterns = [
    path('', views.CustomerListView.as_view(), name='customer_list'),
    path('detail/<int:customer_id>/', views.CustomerDetailView.as_view(), name='customer_detail'),
    path('create/', views.CustomerCreateView.as_view(), name='customer_create'),
    path('edit/<int:customer_id>/', views.CustomerUpdateView.as_view(), name='customer_update'),
    path('delete/<int:customer_id>/', views.CustomerDeleteView.as_view(), name='customer_delete'),

    path('login-page/', auth.login_page, name='login_page'),
    path('register-page/', auth.register_page, name='register_page'),
    path('logout_page/', auth.login_page, name='logout_page')
]
