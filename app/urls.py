from django.contrib import admin
from django.urls import path
from app.views import Index, store, Cart, CheckOut, Login, logout, OrderView, Signup, auth_middleware, product_detail

urlpatterns = [
    path('', Index.as_view(), name='homepage'),
    path('store', store , name='store'),
    path('signup', Signup.as_view(), name='signup'),
    path('login', Login.as_view(), name='login'),
    path('logout', logout , name='logout'),
    path('cart', auth_middleware(Cart.as_view()) , name='cart'),
    path('check-out', CheckOut.as_view() , name='checkout'),
    path('orders', auth_middleware(OrderView.as_view()), name='orders'),
    path('product_detail/<int:id>/',product_detail, name='product_detail' )

]