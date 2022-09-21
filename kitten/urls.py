from django.urls import include, path
from rest_framework import routers
from kitten.views import KittenListView, KittenDetail

# router = routers.SimpleRouter()
# router.register(r'kittens/', KittenViewSet, basename='Kitten')

from django.urls import include, path

urlpatterns = [
    path('kittens/', KittenListView.as_view()),
    path('kittens/<int:pk>/', KittenDetail.as_view())
]
