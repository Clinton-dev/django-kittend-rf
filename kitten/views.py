from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
from .models import Kitten
from .serializer import KittenSerializer


class KittenListView(APIView):
    """
    Lists all kittens or create a new kitten
    """

    def get(self, request, format=None):
        kittens = Kitten.objects.all()
        serializer = KittenSerializer(kittens, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = KittenSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.erros, status=status.HTTP_400_BAD_REQUEST)


class KittenDetail(APIView):
    """
    Retrive, update or delete kitten instance
    """

    def get_object(self, pk):
        try:
            return Kitten.objects.get(pk=pk)
        except Kitten.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        kitten = self.get_object(pk)
        serializer = KittenSerializer(kitten)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        kitten = self.get_object(pk)
        serializer = KittenSerializer(kitten, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        kitten = self.get_object(pk)
        kitten.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
