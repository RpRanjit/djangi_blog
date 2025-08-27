from django.contrib import admin
from .models import Subscriber, EmailTemplate
from django import forms
from django.core.mail import send_mail
from django.conf import settings
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from datetime import datetime

class EmailTemplateAdminForm(forms.ModelForm):
    class Meta:
        model = EmailTemplate
        fields = '__all__'

class EmailTemplateAdmin(admin.ModelAdmin):
    form = EmailTemplateAdminForm

    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)

        # Gather data
        subject = obj.subject
        from_email = settings.EMAIL_HOST_USER
        recipients = [subscriber.email for subscriber in Subscriber.objects.all()]

        # Render HTML message with Bootstrap-styled newsletter
        context = {
            'subject': obj.subject,
            'message': obj.message,
            'year': datetime.now().year,
            'image_url': 'https://via.placeholder.com/600x200.png?text=Your+Banner+Here',  # optional
        }
        html_message = render_to_string('newsletter/newsletter_email.html', context)
        plain_message = strip_tags(obj.message)

        # Send the email
        send_mail(
            subject,
            plain_message,
            from_email,
            recipients,
            html_message=html_message,
            fail_silently=False,
        )

admin.site.register(Subscriber)
admin.site.register(EmailTemplate, EmailTemplateAdmin)

