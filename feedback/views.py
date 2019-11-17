from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic.edit import BaseCreateView
from django.conf import settings

from .models import Feedback
from .forms import FeedbackForm
from .email import send_email_about_feedback


class FeedbackCreate(BaseCreateView):
    model = Feedback
    form_class = FeedbackForm
    success_url = reverse_lazy('index')

    def get(self, request):
        return HttpResponseRedirect('/#contact')

    def form_valid(self, form):

        # check that captcha is set correctly
        if not form.data.get('captcha').lower() in settings.ALLOWED_CAPTCHA_VALUES:
            messages.add_message(self.request, messages.WARNING, 'Error submitting the form. May be you should find correct Policyinsights founder name.')
        else:
            feedback = form.save()
            send_email_about_feedback(self.request, feedback)
            messages.add_message(self.request, messages.SUCCESS, 'Thank you for your message.')
        return HttpResponseRedirect('/#contact')
