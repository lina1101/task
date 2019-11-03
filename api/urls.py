from django.urls import path

from api.views import FibonacciView, FactorialView, AckermannView

urlpatterns = [
    path('factorial/', FactorialView.as_view(), name='factorial-view'),
    path('fibonacci/', FibonacciView.as_view(), name='fibonacci-view'),
    path('ackermann/', AckermannView.as_view(), name='ackermann-view'),
]
