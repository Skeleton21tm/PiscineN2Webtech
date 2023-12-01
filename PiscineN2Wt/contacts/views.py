from django.shortcuts import render
from .forms import ContactForm
from .models import Contact

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            Contact.objects.create(**form.cleaned_data)

        else:
            print('il manque quelque chose ptit con')
    else:
        form = ContactForm()

    return render(request, 'contacts/contacts.html', {'form':form})
