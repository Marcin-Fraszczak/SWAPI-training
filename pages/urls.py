from django.urls import path

from . import views

app_name = 'pages'

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    path('collection/<int:category>/', views.CollectionView.as_view(), name='collection'),
]

