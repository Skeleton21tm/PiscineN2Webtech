from django.urls import path
from blog.views import repertoire, article,formulaire


urlpatterns = [
    path('', repertoire, name='mon_repertoire'),
    path('article/<int:id>/', article, name='mon_article'),
    path('form/', formulaire, name='form'),

]