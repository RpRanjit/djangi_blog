from django.shortcuts import render
from .forms import SubscriberForm
from django.conf import settings
from django.core.mail import send_mail
from django.template.loader import render_to_string

# Create your views here.
def index(request):
    if request.method == 'POST':
        form = SubscriberForm(request.POST)
        if form.is_valid():
            subscriber = form.save()
            # Send confirmation email
            context = {
                'name': subscriber.name,
                'email': subscriber.email,
            }   
            email_content = render_to_string('newsletter/subscription_email.html', context)
            email_subject = 'Thank you for subscribing!'
            recepitent_list = [subscriber.email]
            from_email = settings.EMAIL_HOST_USER
            send_mail(
                email_subject,
                '',
                from_email,
                recepitent_list,
                html_message=email_content,
                fail_silently=False,
            )

            return render(request, 'newsletter/success.html', {'subscriber': subscriber})
    else:
        form = SubscriberForm()
    return render(request, 'newsletter/index.html', {'form': form})
          