from django.contrib import admin
from mptt.admin import DraggableMPTTAdmin
from .models import Category, Product
# from .models import Post
#
#
# class PostAdmin(admin.ModelAdmin):
#     list_display = ('title', 'slug', 'author', 'publish', 'status')


admin.site.register(Category)
admin.site.register(Product)
# admin.site.register(Post)

#
#admin.site.register(Category, DraggableMPTTAdmin)
# admin.site.register(Product, DraggableMPTTAdmin)
