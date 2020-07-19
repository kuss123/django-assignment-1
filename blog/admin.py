from django.contrib import admin
from .models import BlogTable, AuthorTable

admin.site.register(BlogTable)
admin.site.register(AuthorTable)

