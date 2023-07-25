from django.contrib import admin

from django.utils.html import mark_safe

from .models import ProfilePhoto, PersonalInfo, SocialMedia

admin.site.register([ProfilePhoto, PersonalInfo, SocialMedia])


