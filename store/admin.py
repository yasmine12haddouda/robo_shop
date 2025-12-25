from django.contrib import admin
from django.core.exceptions import PermissionDenied
from .models import Product
from accounts.models import Seller


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'seller', 'price', 'stock')

    def get_fields(self, request, obj=None):
        # Superusers can choose the seller; regular seller-users cannot.
        common = ['name', 'price', 'stock', 'description']
        if request.user.is_superuser:
            return ['seller'] + common
        return common

    def save_model(self, request, obj, form, change):
        # If user is a seller, assign their seller relation automatically.
        if request.user.is_superuser:
            # superuser may set seller via form
            super().save_model(request, obj, form, change)
            return

        # Non-superusers must be a Seller
        if hasattr(request.user, 'seller'):
            obj.seller = request.user.seller
            super().save_model(request, obj, form, change)
            return

        raise PermissionDenied("You must be a Seller to add products.")

    def has_add_permission(self, request):
        return request.user.is_active and (request.user.is_superuser or hasattr(request.user, 'seller'))
