from django.urls import path, include

from product import views

urlpatterns = [
    path('latestproducts/', views.LatestProductsList.as_view()),
    path('products/search/', views.search),
    path('products/<slug:category_slug>/<slug:product_slug>/', views.ProductDetail.as_view()),
    path('products/<slug:category_slug>/', views.CategoryDetail.as_view()),
    path('colors/', views.ColorsList.as_view()),
    path('collections/', views.CollectionList.as_view()),
]
