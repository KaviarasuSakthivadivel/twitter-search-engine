from django.urls import path

from . import views

urlpatterns = [
    path('api/search', views.search),
    path('api/get_replies/<str:tweet_id>/', views.get_replies),
    path('api/dashboard',views.get_dashboard_data),
]