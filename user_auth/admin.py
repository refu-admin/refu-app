from django.contrib import admin

# Register your models here.
class StwiuserAdmin(admin.ModelAdmin):
    list_display = ('id','user_id','user_name','user_img','user_text','user_created_at')