from rest_framework import generics, status
from rest_framework.response import Response
from .models import District, LocalArea, Lead
from .serializers import DistrictSerializer, LocalAreaSerializer, LeadSerializer

# ... (Any existing code in views.py)

class LeadCreateView(generics.CreateAPIView):
    queryset = Lead.objects.all()
    serializer_class = LeadSerializer

class DistrictListView(generics.ListAPIView):
    queryset = District.objects.all()
    serializer_class = DistrictSerializer

class LocalAreaListView(generics.ListAPIView):
    serializer_class = LocalAreaSerializer

    def get_queryset(self):
        district_id = self.request.query_params.get('district_id')
        if district_id:
            return LocalArea.objects.filter(district_id=district_id)
        else:
            return LocalArea.objects.none()  # Or return all if no district is selected initially