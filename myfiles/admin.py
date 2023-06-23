from django.contrib import admin
from myfiles.models import Portfolio, Type


# Register your models here.

class AdminPortfolio(admin.ModelAdmin):
    list_display = ['id', 'name', 'company_name', 'deadline', 'type', 'picture1']


admin.site.register(Portfolio, AdminPortfolio)


class AdminType(admin.ModelAdmin):
    list_display = ['id', 'name', ]


admin.site.register(Type, AdminType)
