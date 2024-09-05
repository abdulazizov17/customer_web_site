from django.urls import path
from product import views
from product import auth
from product.auth import ActivateAccountView
urlpatterns = [
    path('', views.ProductListTemplateView.as_view(), name='product_list'),
    path('<int:product_id>/', views.ProductDetailView.as_view(), name='product_detail'),
    path('create/', views.ProductCreateView.as_view(), name='product_create'),
    path('<int:product_id>/edit/', views.ProductUpdateView.as_view(), name='product_update'),
    path('<int:product_id>/delete/', views.ProductDeleteView.as_view(), name='product_delete'),
    # path('grid/<int:product_id>/', views.ProductGridView.as_view(), name='product_grid') ,

    path('login-page/', auth.LoginPage.as_view(), name='login_page'),
    path('register-page/', auth.RegisterPage.as_view(), name='register_page'),
    path('logout_page/', auth.logout_page, name='logout_page'),
    path('send-email/', auth.SendingEmail.as_view(), name = 'sending_email'),
    path('activate/<uidb64>/<token>/', ActivateAccountView.as_view(), name='activate'),
]
