from django.shortcuts import render

def shopping_home(request):
    return render(request, "shopping/index.html")

def shopping_shop(request):
    return render(request, "shopping/shop.html")

def shopping_item(request):
    return render(request, "shopping/item.html")

def shopping_admin(request):
    return render(request, "shopping/admin.html")