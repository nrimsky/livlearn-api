from django.urls import path, include
from rest_framework.routers import DefaultRouter
from django.contrib import admin
from livlearn.api import views

# Create a router and register our viewsets with it.
router = DefaultRouter()

router.register(r'test', views.TestViewSet)

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls)),
]

urlpatterns += [
    path('admin/', admin.site.urls),
]
