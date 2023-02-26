from django.shortcuts import render

from .forms import ContactForm


# date_creation, subject, message, sender, cc_myself
def contact_send(request):
    if request.method == "GET":
        form = ContactForm()
    else:
        form = ContactForm(request.POST, request.FILES)
        if form.is_valid():
            date_creation = form.cleaned_data["date_creation"]
