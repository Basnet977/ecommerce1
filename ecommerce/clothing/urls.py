
from django.urls import path,include 
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'v1',views.ProductApiViews)

urlpatterns = [
    path('',views.home,name='home'),
    path('products',views.products,name='products'),
    path('cat_display/<cat_id>',views.cat_display,name='cat_display'),
    path('about',views.about,name='about'),
    path('product-details/<slug>',views.product_details,name='product-details'),
    path('contact',views.contact,name='contact'),
    path('api/',include(router.urls))
]
