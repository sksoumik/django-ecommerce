from django.shortcuts import render

from .forms import ContactForm


def home_page(request):
    context = {
        "title": "Hello Python!",
        "content": "Welcome to the home page"
    }

    return render(request, 'ecommerce/home_page.html', context)


def about_page(request):
    context = {
        "title": "About Page",
        "content": "Welcome to the home page"

    }
    return render(request, 'ecommerce/home_page.html', context)


def contact_page(request):
    contact_form = ContactForm(request.POST or None)
    context = {
        "title": "Contact page",
        "content": "Welcome to the contact page",
        "form": contact_form
    }
    if contact_form.is_valid():
        print(contact_form.cleaned_data)

    # if request.method == 'POST':
    #     print(request.POST)
    #     print(request.POST.get('fullname'))
    #     print(request.POST.get('email'))
    #     print(request.POST.get('content'))

    return render(request, 'ecommerce/contact/view.html', context)