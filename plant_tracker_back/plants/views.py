from rest_framework import viewsets
from .models import Plant
from .serializers import PlantSerializer
from django.utils import timezone
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework import status
from django.http import QueryDict

class PlantViewSet(viewsets.ModelViewSet):
    queryset = Plant.objects.all().order_by('id')
    serializer_class = PlantSerializer
    parser_classes = (MultiPartParser, FormParser,)
    
    lookup_field = 'slug'
    
    def partial_update(self, request, *args, **kwargs):
        instance = self.get_object()
        data = request.data.dict()
        if data.get('last_time_watered'):
            data['last_time_watered'] = timezone.localtime(timezone.now()).isoformat()
            
        if 'image' in request.data:
            instance.image.delete()  
            instance.image = data['image']
            del data['image']
            
        query_data = QueryDict('', mutable=True)
        query_data.update(data)

        
        serializer = self.get_serializer(instance, data=query_data, partial=True)  
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def create(self, request, *args, **kwargs):
        print(request.data)
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

