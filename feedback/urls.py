from django.urls import path
from django.views.generic import TemplateView

from feedback import views


urlpatterns = [
    path('feedback/', views.FeedbackCreate.as_view(), name='feedback'),
]

