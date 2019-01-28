from django.contrib import admin
from .models import Users,Talk

@admin.register(Users)
class UsersAdmin(admin.ModelAdmin):
    pass

@admin.register(Talk)
class TalkAdmin(admin.ModelAdmin):
    pass