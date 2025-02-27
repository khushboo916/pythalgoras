from django.contrib import admin
from .models import Profile

admin.site.register(Profile)

admin.site.site_header = "My Custom Admin Panel"
admin.site.site_title = "My Admin Portal"
admin.site.index_title = "Welcome to My Custom Admin"
