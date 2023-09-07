from django.http import Http404
from rest_framework import status, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Resource
from .serializers import ResourceSerializer
from api.permissions import IsOwnerOrReadOnly


class ResourceList(APIView):
    serializer_class = ResourceSerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly
    ]

    def get(self, request):
        resources = Resource.objects.all()
        serializer = ResourceSerializer(
            resources, many=True, context={'request': request}
        )
        return Response(serializer.data)

    def resource(self, request):
        serializer = ResourceSerializer(
            data=request.data, context={'request': request}
        )
        if serializer.is_valid():
            serializer.save(owner=request.user)
            return Response(
                serializer.data, status=status.HTTP_201_CREATED
            )
        return Response(
            serializer.errors, status=status.HTTP_400_BAD_REQUEST
        )


class ResourceDetail(APIView):
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = ResourceSerializer

    def get_object(self, pk):
        try:
            resource = Resource.objects.get(pk=pk)
            self.check_object_permissions(self.request, resource)
            return resource
        except Resource.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        resource = self.get_object(pk)
        serializer = ResourceSerializer(
            resource, context={'request': request}
        )
        return Response(serializer.data)

    def put(self, request, pk):
        resource = self.get_object(pk)
        serializer = ResourceSerializer(
            resource, data=request.data, context={'request': request}
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(
            serializer.errors, status=status.HTTP_400_BAD_REQUEST
        )

    def delete(self, request, pk):
        resource = self.get_object(pk)
        resource.delete()
        return Response(
            status=status.HTTP_204_NO_CONTENT
        )