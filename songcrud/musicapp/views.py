from django.http import HttpResponse
from .models import Song, Artiste
from .serializers import ArtisteSerializer, SongSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
# Create your views here.
def index(request):
    return HttpResponse('Hello this is my first Django project')

@api_view(['GET', 'POST'])
def Song_list(request):

    if request.method == 'GET':
        song = Song.objects.all()
        serializer = SongSerializer(song, many = True)
        return Response(serializer.data,)
    
    if request.method == 'POST':
        serializer = SongSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
@api_view(['GET', 'PUT', 'DELETE'])
def Song_detail(request, id):

    try:
        song=Song.objects.get(pk=id)
    except Song.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = SongSerializer(song)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = SongSerializer(song, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        song.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


        
        
@api_view(['GET', 'POST'])
def Artiste_list(request):
    

    if request.method == 'GET':
        artiste = Artiste.objects.all()
        serializer = ArtisteSerializer(artiste, many=True)
        return Response(serializer.data)
    
    if request.method == 'POST':
        serializer = ArtisteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
@api_view(['GET', 'PUT', 'DELETE'])
def Artiste_detail(request, id):

    try:
        artiste = Artiste.objects.get(pk=id)
    except Artiste.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = ArtisteSerializer(artiste)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = ArtisteSerializer(artiste, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        artiste.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

