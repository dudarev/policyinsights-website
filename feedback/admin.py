from django.contrib import admin

# Register your models here.

from .models import Feedback, FeedbackEmail


class FeedbackAdmin(admin.ModelAdmin):
    readonly_fields = ('submitted_at',)
    search_fields = ('name', 'email', 'content',)


admin.site.register(Feedback, FeedbackAdmin)
admin.site.register(FeedbackEmail)
