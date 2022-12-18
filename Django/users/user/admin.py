from django.contrib import admin
from .models import TelegramUser, UserInfo

# Register your models here.


class InfoUser(admin.TabularInline):
    model = UserInfo
    extra = 0


class ArticleUser(admin.ModelAdmin):
    inlines = [InfoUser]


admin.site.register(TelegramUser, ArticleUser)
admin.site.register(UserInfo)