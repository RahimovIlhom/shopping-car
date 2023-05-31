from django.shortcuts import get_object_or_404
from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import Car
from .serializers import CarSerializer


class CarViewSet(viewsets.ViewSet):
    queryset = Car.objects.all()
    serializer_class = CarSerializer

    def list(self, request):
        queryset = self.queryset.filter(is_active=True)
        serializers = CarSerializer(queryset, many=True, context=self.get_serializers_context())
        return Response(serializers.data)

    def retrieve(self, request, pk=None):
        comment = get_object_or_404(self.queryset, pk=pk)
        serilizers = CarSerializer(comment, context=self.get_serializers_context())
        return Response(serilizers.data)

    def create(self, request, *args, **kwargs):
        serializer = CarSerializer(data=request.data, context=self.get_serializers_context())
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        car = get_object_or_404(self.queryset, pk=pk)
        serializer = CarSerializer(car, context=self.get_serializers_context())
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def partial_update(self, request, pk=None):
        car = get_object_or_404(self.queryset, pk=pk)
        serializer = CarSerializer(car, partial=True, context=self.get_serializers_context())
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        car = get_object_or_404(self.queryset, pk=pk)
        if car.is_active:
            car.is_active = False
            car.save()
        else:
            car.is_active = True
            car.save()
        serializer = CarSerializer(car, context=self.get_serializers_context())
        return Response(serializer.data, status=status.HTTP_204_NO_CONTENT)

    def get_serializers_context(self):
        return {'request': self.request}


class BusyCarViewSet(viewsets.ViewSet):
    queryset = Car.objects.filter(is_active=False)
    serializer_class = CarSerializer

    def list(self, request):
        serializers = CarSerializer(self.queryset, many=True, context=self.get_serializers_context())
        return Response(serializers.data)

    def retrieve(self, request, pk=None):
        car = get_object_or_404(self.queryset, pk=pk)
        serilizers = CarSerializer(car, context=self.get_serializers_context())
        return Response(serilizers.data)

    def update(self, request, pk=None):
        car = get_object_or_404(self.queryset, pk=pk)
        serializer = CarSerializer(car, context=self.get_serializers_context())
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def partial_update(self, request, pk=None):
        car = get_object_or_404(self.queryset, pk=pk)
        serializer = CarSerializer(car, partial=True, context=self.get_serializers_context())
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        car = get_object_or_404(self.queryset, pk=pk)
        car.is_active = True
        car.save()
        if car.is_active:
            car.is_active = False
            car.save()
        else:
            car.is_active = True
            car.save()
        serializer = CarSerializer(car, context=self.get_serializers_context())
        return Response(serializer.data, status=status.HTTP_204_NO_CONTENT)

    def get_serializers_context(self):
        return {'request': self.request}
