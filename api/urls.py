from django.urls import path
from api.views import *



urlpatterns = [
    
    path('', ArticlesList.as_view()),
    path('<int:pk>/', ArticlesDetail.as_view()),
    
]
