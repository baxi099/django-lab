# views.py
from django.shortcuts import render
from .forms import RegistrationForm

def registration_view(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            return render(request, 'details.html', {'data': data})
    else:
        form = RegistrationForm()
    return render(request, 'registration_form.html', {'form': form})
