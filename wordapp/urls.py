from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register('word', views.WordViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('get/politics/', views.politics_get_api),
    path('get/society/', views.society_get_api),
    path('get/economy/', views.economy_get_api),
    path('get/military/', views.military_get_api),
    path('get/culture/', views.culture_get_api),
    path('get/it_science/', views.it_science_get_api),
]