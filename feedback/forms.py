from django.forms import CharField, ModelForm, Textarea

from .models import Feedback


class FeedbackForm(ModelForm):
    captcha = CharField()  # possible values are defined in settings.ALLOWED_CAPTCHA_VALUES

    class Meta:
        model = Feedback
        fields = ['name', 'email', 'content', 'captcha']
