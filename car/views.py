from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
from .serializers import CarSerializer
from .models import Car


class CarAPIView(APIView):
    def get(self, request):
        car = Car.objects.all()
        return Response({'posts': CarSerializer(car, many=True).data})


    def post(self, request):
        serializer = CarSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({'post':serializer.data})

    def put(self, request, *args, **kwargs ):
        pk = kwargs.get("pk", None)
        if not pk:
            return Response({"error": "Method not allowed"})

        try:
            instance = Car.objects.get(pk=pk)
        except:
            return Response({"error": "Object does not exists"})

        serializer = CarSerializer(data=request.data, instance=instance)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({"post": serializer.data})

    def delete(self, request, *args, **kwargs):
        pk = kwargs.get("pk", None)
        if not pk:
            return Response({"error": "Method DELETE not allowed"})

        try:
            instance = Car.objects.get(pk=pk)
        except:
            return Response({"error": "Object does not exists"})

        if instance:
            instance.delete()

            return Response({"post": "delete post " + str(pk)})


class CarAPIList(generics.ListCreateAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer