from django.templatetags.static import static
from django.urls import path

from config import settings
from users import views
urlpatterns = [
    path('login-page/', views.login_page, name='login_page'),
    path('register-page/', views.register_page, name='register_page'),
    path('logout_page/', views.login_page, name='logout_page')
]