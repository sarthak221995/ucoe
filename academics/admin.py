from django.contrib import admin
from .models import Post

class PostAdmin(admin.ModelAdmin):
	list_filter = ['created','text']
	list_display = ('text','created','modified')


admin.site.register(Post,PostAdmin)