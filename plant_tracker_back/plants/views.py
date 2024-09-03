from rest_framework import viewsets
from .models import Plant
from .serializers import PlantSerializer
from django.utils import timezone
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework import status

class PlantViewSet(viewsets.ModelViewSet):
    queryset = Plant.objects.all().order_by('last_time_watered')
    serializer_class = PlantSerializer
    parser_classes = (MultiPartParser, FormParser,)
    
    lookup_field = 'slug'
    
    def partial_update(self, request, *args, **kwargs):
        instance = self.get_object()
        data = request.data.dict()
        data['last_time_watered'] = timezone.localtime(timezone.now()).isoformat()
        serializer = self.get_serializer(instance, data=data, partial=True)

        if 'image' in request.data:
            instance.image.delete()  
            instance.image = request.data['image']  

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

