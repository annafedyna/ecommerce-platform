from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Product, Category, UserProfile

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("title", "price")
# admin.site.register(ProductAdmin, Product)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "slug")
# admin.site.register(CategoryAdmin, Category)

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = (
        'username',
        'email',
        'stripe_customer_id',
        'one_click_purchasing',
    )
    search_fields = (
        'user__username',
        'user__email',
        'stripe_customer_id',
    )
    list_filter = (
        'one_click_purchasing',
    )
    ordering = (
        'user__username',
    )
    list_select_related = ('user',)
    readonly_fields = ('user',)

    def username(self, obj):
        return obj.user.username

    def email(self, obj):
        return obj.user.email

    username.admin_order_field = 'user__username'
    email.admin_order_field = 'user__email'
