from django.contrib import admin

from .models import EmailVerification, User

admin.site.register(User)
admin.site.register(EmailVerification)
