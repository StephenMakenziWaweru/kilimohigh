from django.urls import path
from .views import (StudentListView, StudentCreateView,
                    StudentDetailView, StudentDeleteView,
                    StudentUpdateView)


urlpatterns = [
    path('', StudentListView.as_view(), name = 'home'),
    path('create/', StudentCreateView.as_view(), name = 'create'),
    path('detail/<int:pk>', StudentDetailView.as_view(), name = 'detail'),
    path('delete/<int:pk>', StudentDeleteView.as_view(), name = 'delete'),
    path('update/<int:pk>', StudentUpdateView.as_view(), name = 'update'),
]
