from django.urls import path
from .import views


urlpatterns = [
    
    path('register/',views.registerPage, name="register"),
    path('login/',views.loginPage, name="login"),


    path('',views.home, name="home"),
    path('products/',views.products, name="products"),
    path('customer/',views.registerPage, name="register")
]