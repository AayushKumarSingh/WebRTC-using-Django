from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template import loader
from .models import BloodDonor, BloodRequest
from .forms import BloodDonationForm, BloodRequestForm

# Create your views here.


def homepage_view(request, *args, **kwargs):
    print(request)
    print(request.user)
    # return HttpResponse("<h1>Hello World</h1>")
    return render(request, "home.html", {})


def contact_view(request, *args, **kwargs):
    return render(request, "contact.html", {})


def social_view(request, *args, **kwargs):
    content = loader.render_to_string("socials.html", context=None, request=request, using=None)
    return HttpResponse(content, content_type=None, status=None)


def success_page(request):
    return render(request, 'success_page.html')


def blood_donation_form(request):
    if request.method == 'POST':
        form = BloodDonationForm(request.POST)
        if form.is_valid():
            form.save()
            # Process the form data (e.g., save to database)
            # Redirect to a success page or another URL
            return redirect('success_page')  # Redirect to a success page
    else:
        form = BloodDonationForm()

    return render(request, 'blood_donation_form.html', {'form': form})


def blood_request_form(request):
    if request.method == 'POST':
        form = BloodRequestForm(request.POST)
        if form.is_valid():
            # Extract data from the form
            blood_group = form.cleaned_data['blood_group']
            quantity = form.cleaned_data['quantity']

            # Save the data to the database
            BloodRequest.objects.create(blood_group=blood_group, quantity=quantity)

            return redirect('success_page')  # Redirect to a success page
    else:
        form = BloodRequestForm()

    return render(request, 'blood_request_form.html', {'form': form})
