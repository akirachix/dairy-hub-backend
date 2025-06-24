from  django.urls import path, include

from  rest_framework.routers import DefaultRouter

from  .views import OrderItemsViewSet

router=DefaultRouter()

router.register(r"orderItems", OrderItemsViewSet, basename="orderItems")

urlpatterns=[
    path("", include(router.urls)),
]