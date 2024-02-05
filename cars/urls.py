from django.urls import path, include
from . import views
from .views import DetailPostView

urlpatterns = [
    
    path('details/<int:id>/', views.DetailPostView.as_view(), name = 'detail_post'),
     path('buy/<int:id>/', views.buyNow, name='buyNow'),
]
