from .models import Word
from rest_framework import viewsets
from .serializers import WordSerializer
from rest_framework import status 
from rest_framework.decorators import api_view 
from rest_framework.response import Response 
from django.http.response import HttpResponse

class WordViewSet(viewsets.ModelViewSet):
    queryset = Word.objects.all()
    serializer_class = WordSerializer

@api_view(['GET'])
def politics_get_api(request):
    politics = Word.objects.filter(genre__contains="politics")
    serialized_politics = WordSerializer(politics, many=True)
    return Response(serialized_politics.data)

@api_view(['GET'])
def society_get_api(request):
    society = Word.objects.filter(genre__contains="society")
    serialized_politics = WordSerializer(society, many=True)
    return Response(serialized_politics.data)

@api_view(['GET'])
def economy_get_api(request):
    economy = Word.objects.filter(genre__contains="economy")
    serialized_politics = WordSerializer(economy, many=True)
    return Response(serialized_politics.data)

@api_view(['GET'])
def military_get_api(request):
    military = Word.objects.filter(genre__contains="military")
    serialized_politics = WordSerializer(military, many=True)
    return Response(serialized_politics.data)

@api_view(['GET'])
def culture_get_api(request):
    culture = Word.objects.filter(genre__contains="culture")
    serialized_politics = WordSerializer(culture, many=True)
    return Response(serialized_politics.data)

@api_view(['GET'])
def it_science_get_api(request):
    it_science = Word.objects.filter(genre__contains="it_science")
    serialized_politics = WordSerializer(it_science, many=True)
    return Response(serialized_politics.data)