from django.contrib import admin
from .models import User
# admin.site.register(User)
class PostStudent(admin.ModelAdmin):
    list_display = ['id','name','email','age','date','gender']
    list_filter = ['date']
    search_fields = ['name','email']
admin.site.register(User,PostStudent)
# Register your models here.
