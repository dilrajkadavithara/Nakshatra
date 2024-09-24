from django.urls import path
from . import views

urlpatterns = [
    path('leads/', views.LeadCreateView.as_view(), name='lead-create'),
    path('districts/', views.DistrictListView.as_view(), name='district-list'),
    path('local-areas/', views.LocalAreaListView.as_view(), name='local-area-list'),
]