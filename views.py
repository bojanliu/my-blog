from django.shortcuts import render_to_response
from myblog.forms import contactform
from django.http import HttpResponseRedirect
from django.core.mail import send_mail
from django.views.decorators.csrf import csrf_exempt

def contact(request):
    if request.method=='POST':
        form=contactform(request.POST)
        if form.is_valid():
            human=True
            cd=form.cleaned_data
            send_mail(
                cd['subject'],
                cd['message'],
                cd.get('email','noreply@example.com'),
                ['******@gmail.com'],
                )
            return HttpResponseRedirect('/contact/thanks/')
    else:
        form=contactform()
    return render_to_response('contact/contact_form.html',{'form':form})
        

    
