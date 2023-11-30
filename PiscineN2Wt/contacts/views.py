from django.shortcuts import render, redirect
from .forms import ContactForm

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            ContactForm.objects.create(**form.cleaned_data)

            # Process contact form data here

            return redirect('liste_contact')
        else:
            form = ContactForm()
    else:
        form = ContactForm()

    return render(request, 'contacts/contacts.html', {'form':form})
