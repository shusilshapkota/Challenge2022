from django.shortcuts import render, redirect
from rest_framework.response import Response
from rest_framework import status
from .models import UserImages
from .serializers import UserImagesSerializer
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser
import math

# Create your views here.
class postImage(APIView):
    parser_classes = [MultiPartParser, FormParser]

    def post(self, request, format=None):
        print(request.data)
        private = False
        all_valid = False
        data = request.data
        serializer_errors = ""
        img_list = request.FILES.getlist("image")

        for count, x in enumerate(img_list):
            data._mutable = True
            data['image'] = img_list[count]
            data._mutable = False

            serializer = UserImagesSerializer(data=data)

            if serializer.is_valid():
                serializer.save()
                all_valid = True
            else:
                all_valid = False
                serializer_errors = serializer.errors

        if all_valid:
            return Response("All images posted", status=status.HTTP_200_OK)
        else:
            if serializer_errors:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

            return Response("Something went wrong!", status=status.HTTP_400_BAD_REQUEST)


class profilePage(APIView):
    def get(self, request):
        imgs = UserImages.objects.filter(user=1)
        num_of_cols = 3
        new_img_list = []

        rows = math.ceil(imgs.count()/num_of_cols)
        start, end = 0, rows

        for i in range(num_of_cols):
            new_img_list.append(imgs[start:end])
            start, end = end, end+rows

        context = {"pics": new_img_list}

        return render(request, 'profilePage.html', context)
