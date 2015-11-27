from django.contrib import admin

from .models import Quote, Category


class QuoteAdmin(admin.ModelAdmin):
    pass
admin.site.register(Quote, QuoteAdmin)
class CategoryAdmin(admin.ModelAdmin):
    pass
admin.site.register(Category, CategoryAdmin)
