from rest_framework import viewsets
from .models import Plant
from .serializers import PlantSerializer
from django.utils import timezone

class PlantViewSet(viewsets.ModelViewSet):
    queryset = Plant.objects.all().order_by('last_time_watered')
    serializer_class = PlantSerializer
    lookup_field = 'slug'

    def partial_update(self, request, *args, **kwargs):
        instance = self.get_object()
        last_time_watered= request.data.get('last_time_watered')
        if last_time_watered:
            print(timezone.localtime(timezone.now()))
            request.data['last_time_watered'] = timezone.localtime(timezone.now()).isoformat()
        return super().partial_update(request, *args, **kwargs)
