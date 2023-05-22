from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
path('store/', views.store, name = "store"),
path('cart/', views.cart, name = "cart"),
path('profile/', views.profile, name = "profile"),
path('checkout/', views.checkout, name = "checkout"),

path('dealer_register/', views.dealer_register, name = "dealer_register"),
path('dealer_info/', views.dealer_info, name = "dealer_info"),
path('dealer_login/', views.dealer_login, name = "dealer_login"),
path('dealer_home/', views.dealer_home, name = "dealer_home"),
path('dealer_product/', views.dealer_product, name = "dealer_product"),
path('dealer_logout/', views.dealer_logoutsite, name = "dealer_logout"),

path('register/', views.register, name = "register"),
path('', views.login, name = "login"),
path('logout/', views.logoutsite, name = "logout"),
path('info/', views.info, name = "info"),

path('require/', views.require, name = "require"),
path('require_delete/<int:require_id>', views.delete_require, name="require_delete"),
path('search/', views.search, name = "search"),
path('product/<int:product_id>', views.product, name = "product"),
path('category/<int:category_id>', views.category, name = "category"),
path('entity/<int:entity_id>', views.entity, name = "entity"),
path('order_placed/<int:orderItem_id>', views.order_placed, name="order_placed"),
path('order_detail/<int:orderItem_id>', views.order_detail, name="order_detail"),

path('update_item/', views.updateItem, name = "update_item"),
path('process_order/', views.processOrder, name = "process_order"),

path('reset_password/', auth_views.PasswordResetView.as_view(template_name="store/passwords/reset_password.html"), name="reset_password"),
path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name="store/passwords/password_reset_done.html"), name="password_reset_done"),
path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="store/passwords/password_reset_confirm.html"), name="password_reset_confirm"),
path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name="store/passwords/password_reset_complete.html"), name="password_reset_complete"),
]
