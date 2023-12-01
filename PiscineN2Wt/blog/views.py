from .models import MonPost
from django.shortcuts import render,get_object_or_404
from .forms import CommentModelForm

def repertoire(request):
    title = "ACTU FOOT DE ZINZIN"
    articles = MonPost.objects.all()
    context = {
        'articles': articles,
        'title': title,
        'name': 'TOUS FOU DE FOOT ET FUCK LES FEMMES'
    }
    return render(request, 'blog/repertoire.html',context)


def article(request, id):
    article = get_object_or_404(MonPost, pk=id)
    return render(request, 'blog/article.html',{'article':article})

 
def formulaire(request):
    message = 'veuillez creer votre article'
    
    if request.method == 'POST':
        form = CommentModelForm(request.POST)
        if form.is_valid():
            MonPost.objects.create(**form.cleaned_data)
            
        else:
            print('il manque quelque chose ptit con')
    else:
            form = CommentModelForm()
        
    return render(request, 'blog/formulaire.html', {'formulaire': form, 'message': message })