from django.contrib import admin

from .models import CreditCard


class CreditCardAdmin(admin.ModelAdmin):
    readonly_fields = ("number", "created_at", "updated_at")

    list_display = ("holder", "brand", "created_at", "updated_at")


admin.site.register(CreditCard, CreditCardAdmin)
