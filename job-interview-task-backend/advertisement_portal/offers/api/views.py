from rest_framework import generics, mixins
from rest_framework import viewsets
from rest_framework.response import Response

from ..models import Offer, Category
from .serializers import CategorySerializer, OfferSerializer


class CategoriesViewSet(viewsets.ViewSet):
    """
    A simple ViewSet for listing categories.
    """
    def list(self, request):
        queryset = Category.objects.all()
        serializer = CategorySerializer(queryset, many=True)
        return Response(serializer.data)


class CategoriesUpdateDeleteCreate(mixins.RetrieveModelMixin, mixins.CreateModelMixin,
                                   mixins.UpdateModelMixin, mixins.DestroyModelMixin,
                                   generics.GenericAPIView):
    """
    A simple Mixin class for single category with POST, PUT and DELETE option
    """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def get(self, request, pk):
        return self.retrieve(request, pk)

    def put(self, request, pk):
        return self.update(request, pk)

    def delete(self, request, pk):
        return self.destroy(request, pk)

    def post(self, request, pk):
        return self.create(request, pk)


class OffersViewSet(viewsets.ViewSet):
    """
    A simple ViewSet for listing offers.
    """
    def list(self, request):
        queryset = Offer.objects.all()
        serializer = OfferSerializer(queryset, many=True)
        return Response(serializer.data)



class OffersUpdateDeleteCreate(mixins.RetrieveModelMixin, mixins.CreateModelMixin,
                                mixins.UpdateModelMixin, mixins.DestroyModelMixin,
                                generics.GenericAPIView):
    """
    A simple Mixin class for single offer with POST, PUT and DELETE option
    """
    queryset = Offer.objects.all()
    serializer_class = OfferSerializer

    def get(self, request, pk):
        return self.retrieve(request, pk)

    def put(self, request, pk):
        return self.update(request, pk)

    def delete(self, request, pk):
        return self.destroy(request, pk)

    def post(self, request, pk):
        return self.create(request, pk)
