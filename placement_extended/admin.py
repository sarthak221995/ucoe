from django.contrib import admin
from .models import Post



class PostAdmin(admin.ModelAdmin):
	list_filter = ['created','modified']
	list_display = ('created','modified')

admin.site.register(Post,PostAdmin)

