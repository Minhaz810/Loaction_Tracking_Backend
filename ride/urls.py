from django.urls import path, include
from .views import TipsListView

urlpatterns = [
    path('tips/', TipsListView.as_view()),
]
