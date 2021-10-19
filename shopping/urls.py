from django.urls import path

from shopping import views

urlpatterns = [
    path("", views.shopping_home),
    path("shop/", views.shopping_shop),
    path("item/", views.shopping_item),
    path("admin/", views.shopping_admin),
]