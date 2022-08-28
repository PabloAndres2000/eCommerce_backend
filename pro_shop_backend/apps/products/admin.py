
# Django
from django.contrib import admin

# Models
from pro_shop_backend.apps.products.models import Product


@admin.register(Product)
class UserAdmin(admin.ModelAdmin):
    """
    User model admin.
    """

    list_display = ('user', 'name', 'brand',
                    'category', 'rating')
