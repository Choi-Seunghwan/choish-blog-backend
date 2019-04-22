from django.shortcuts import render
from rest_framework.parsers import FileUploadParser
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.generics import CreateAPIView

from .serializers import FileSerializer

from rest_framework.response import Response
from rest_framework import status
import os
from .forms import FileForm
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse

# Create your views here.

@csrf_exempt
def fileUpload(request):
    form = FileForm(request.POST, request.FILES)
    form.save()


    return HttpResponse('')


class FileUploadView(CreateAPIView):
    # parser_classes = (FileUploadParser, )
    
    def post(self, request, filename, format=None):
        file_serializer = FileSerializer(data=request.data)
        # file_obj = request.FILES['file']
        # path = '/media/'
        # os.makedirs(path)
        # destination = open(path + file_obj.name, 'wb+')
        # destination.write(file_obj.read())
        # destination.close()

        # form = FileForm(request.POST, request.FILES)
        # form.save()        

        if file_serializer.is_valid():
            file_serializer.save()
            return Response(file_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

