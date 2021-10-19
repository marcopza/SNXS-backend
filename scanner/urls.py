from django.urls import path
from .views import ScannerView

urlpatterns = [
    path('', ScannerView.as_view(), name='test')
]
