from django.shortcuts import render, redirect
from .forms import ContactForm
from .models import Contact

def display_records(request):  
    contacts = Contact.objects.all()
    return render(request, 'my_app_4/records_overview.html', {'contacts': contacts})



def modify_record(request, id):  
    contact = Contact.objects.get(id=id)
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            formdata = form.cleaned_data
            contact.name = formdata['name']
            contact.address = formdata['address']
            contact.profession = formdata['profession']
            contact.tel_number = formdata['tel_number']
            contact.email_address = formdata['email_address']
            contact.save()
            return redirect('completion')  
    else:
        form = ContactForm(initial={
            'name': contact.name,
            'address': contact.address,
            'profession': contact.profession,
            'tel_number': contact.tel_number,
            'email_address': contact.email_address
        })

    return render(request, 'my_app_4/modify_record.html', {'form': form})

def add_record(request):  
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            formdata = form.cleaned_data
            Contact.objects.create(
                name=formdata['name'],
                address=formdata['address'],
                profession=formdata['profession'],
                tel_number=formdata['tel_number'],
                email_address=formdata['email_address']
            )
            return redirect('completion')  
    else:
        form = ContactForm()
    
    return render(request, 'my_app_4/new_record.html', {'form': form})

def completion(request):  
    return render(request, 'my_app_4/operation_complete.html')

def remove_record(request, id): 
    contact = Contact.objects.get(id=id)
    if request.method == 'POST':
        contact.delete()
        return redirect('completion')  
    return render(request, 'my_app_4/remove_record.html', {'contact': contact})
