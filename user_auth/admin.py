from django.contrib import admin
from .models import OAuthTokenTemp

# Register your models here.
admin.site.register(OAuthTokenTemp)

class StwiuserAdmin(admin.ModelAdmin):
    list_display = ('id','user_id','user_name','user_img','user_text','user_created_at')