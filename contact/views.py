from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.mail import EmailMessage

from .forms import ContactForm

# Create your views here.

def contacto(request):
    #print("Tipo de Peticion: {}".format(request.method))
    contact_form = ContactForm()

    if request.method == "POST":
        contact_form = ContactForm(data=request.POST)
        if contact_form.is_valid(): #Devuelve true si todos los campos del formulario estan bien
            name = request.POST.get('name', '')
            email = request.POST.get('email' , '')
            content = request.POST.get('content', '')
            #Suponemos que todo ha salido bien, redireccionamos
            #return redirect("/contact/?ok")
            # Esto es igual a lo anterior

            # Realizamos el envio del correo, con los datos introducidos por el usuario y redireccionamos  
            email = EmailMessage(
                "Nuevo Mensaje de Contacto",
                "De {} <{}>\nEscribió:\n\n{}".format(name,email,content),
                "no-repy@inbox.mailtrap.io",
                ["xxxxxx@gmail.com"],
                reply_to=[email]
            )

            try:
                email.send()
                return redirect(reverse('contact')+"?ok")
            except:
                return redirect(reverse('contact')+"?fail")

    
    return render(request,'contact/contact.html', {'form': contact_form })
