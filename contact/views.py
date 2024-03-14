from django.shortcuts import render, redirect
from django.shortcuts import reverse
from django.core.mail import EmailMessage

from .forms import ContactForm

# Create your views here.
def contact(request):
    contact_form=ContactForm()
    if request.method=='POST':
        contact_form=ContactForm(data=request.POST)
        if contact_form.is_valid():
            name=request.POST.get('name','')
            email=request.POST.get('email','')
            message=request.POST.get('message','')

            #enviar el email
            email=EmailMessage(
                'Mensaje de contacto web recibido',
                'Mensaje enviado por {} <{}>:\n\n{}'.format(name,email,message),
                email,
                ["5102e4edc6db92@inbox.mailtrap.io"],
                reply_to=[email],   
            )
            try:
                email.send()
                #esta todo OK
                return redirect(reverse('contact')+'?ok')
            except:
                #ha habido algún error
                return redirect(reverse('contact')+'?error')
        
    return render(request, 'contact/contact.html', {'form': contact_form})