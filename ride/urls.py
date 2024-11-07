from django.urls import path, include
from .views import TipsListView,AdminEarningListAPIView

urlpatterns = [
    path('tips/', TipsListView.as_view()),
    path('admin-earnings/',AdminEarningListAPIView.as_view())
]
