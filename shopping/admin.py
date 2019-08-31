from django.contrib import admin
from .models import UserCart
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

admin.site.register(UserCart)

class UserCartInline(admin.StackedInline):
	model = UserCart
	can_delete = False
	verbose_name_plural = 'usercart'



class UserAdmin(BaseUserAdmin):
	inlines = (UserCartInline,)

admin.site.unregister(User)
admin.site.register(User, UserAdmin)


# Register your models here.
