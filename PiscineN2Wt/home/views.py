from django.shortcuts import render
from .models import Article
from .forms import RechercheForm

def recherche_articles(request):
    if request.method == 'GET':
        form = RechercheForm(request.GET)
        if form.is_valid():
            terme_recherche = form.cleaned_data['recherche']
            articles = Article.objects.filter(titre__icontains=terme_recherche)
            return render(request, 'home/recherche.html', {'articles': articles, 'form': form})
    else:
        form = RechercheForm()

    return render(request, 'home/recherche.html', {'form': form})

