from django.urls import path
from .views import (StreamListView, StreamCreateView,
                    StreamDetailView)


urlpatterns = [
    path('', StreamListView.as_view(), name = 'stream-home'),
    path('create/', StreamCreateView.as_view(), name = 'stream-create'),
    path('detail/<int:pk>', StreamDetailView.as_view(), name = 'stream-detail'),
#     path('delete/<int:pk>', StreamDeleteView.as_view(), name = 'delete'),
#     path('update/<int:pk>', StreamUpdateView.as_view(), name = 'update'),
]
