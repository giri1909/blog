from django.contrib import admin

# Register your models here.
from django.contrib import admin

from .models import Post
# Register your models here.
admin.site.register(Post)

from .models import EnqDB

# Register your models here.
class EnqDBAdmin(admin.ModelAdmin):
	list_display=['name','mail','mno','message']

admin.site.register(EnqDB,EnqDBAdmin)