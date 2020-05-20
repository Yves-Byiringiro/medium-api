from django.shortcuts import render
from rest_framework import generics
from api.serializers import ArticleSerializer
from api.models import *
from api.permissions import IsAuthorOrReadyOnly




class ArticlesList(generics.ListCreateAPIView):
    queryset            = Article.objects.all()
    serializer_class    = ArticleSerializer
 
    



class ArticlesDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset            = Article.objects.all()
    serializer_class    = ArticleSerializer
    permission_classes  = (IsAuthorOrReadyOnly,)
    
