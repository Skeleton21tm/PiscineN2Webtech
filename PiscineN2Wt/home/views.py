from django.shortcuts import render
import datetime
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.views import View
from django.contrib.auth.decorators import login_required
def home(request):
    current_year = datetime.datetime.now().year
    return render(request, 'home/home.html', {'current_year': current_year})

class RegisterView(View):
    template_name = 'home/register.html'

    def get(self, request):
        form = UserCreationForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Redirige vers la page de connexion après l'enregistrement

        return render(request, self.template_name, {'form': form})

@login_required
def ma_vue_protegee(request):
    # votre code ici
    return render(request, 'home/ma_vue_protegee.html')



