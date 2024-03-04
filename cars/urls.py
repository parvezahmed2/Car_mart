from django.urls import path, include
from . import views
from .views import DetailPostView

urlpatterns = [
    
    path('details/<int:id>/', views.DetailPostView.as_view(), name = 'detail_post'),
     path('buy/<int:car_id>/', views.buyNow.as_view(), name='buyNow'),
]
