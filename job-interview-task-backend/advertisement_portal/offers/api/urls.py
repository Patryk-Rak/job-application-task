from django.urls import path
from . import views

app_name = 'offers_api'
urlpatterns = [
    path('categories/', views.CategoriesViewSet.as_view({'get': 'list'}), name='categories_list'),
    path('categories/<int:pk>/', views.CategoriesUpdateDeleteCreate.as_view(), name='categories_update_delete_post'),
    path('offers/', views.OffersViewSet.as_view({'get': 'list'}), name='offers_list'),
    path('offers/<int:pk>/', views.OffersUpdateDeleteCreate.as_view(), name='offers_update_delete_post'),
]