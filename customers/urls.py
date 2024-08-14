from django.urls import path
from customers import views
from customers import auth
urlpatterns = [
    path('', views.customer_list, name='customer_list'),
    path('detail/<int:customer_id>/', views.customer_detail, name='customer_detail'),
    path('create/', views.customer_create, name='customer_create'),
    path('edit/<int:customer_id>/', views.customer_update, name='customer_update'),
    path('delete/<int:customer_id>/', views.customer_delete, name='customer_delete'),


# authontifacation

    path('login-page/' , auth.login_page, name = 'login_page'),
    path('register-page/', auth.register_page, name='register_page'),
    path('logout_page/',auth.login_page, name='logout_page')


]
