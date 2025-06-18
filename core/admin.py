from django.contrib import admin
from .models import Category, Expense
# Register your models here.


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'user']

@admin.register(Expense)
class ExpenseAdmin(admin.ModelAdmin):
    list_display = ['user', 'category', 'amount', 'date']
    list_filter = ['date', 'category']
    search_fields = ['description']