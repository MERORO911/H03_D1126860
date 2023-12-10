from django.contrib import admin
from .models import Member


class MemberAdmin(admin.ModelAdmin):
    list_display = ('get_fullname', 'age' , 'phone', 'joined_date')

    def get_fullname(self, obj):
        return f"{obj.firstname} {obj.lastname}"
    get_fullname.short_description = 'Full Name'

    def age(self, obj):
        return obj.age

    def phone(self, obj):
        return obj.phone

    def joined_date(self, obj):
        return obj.joined_date
    age.short_description = 'Age'  # 指定 'Age' 給 age 方法的 short_description
    phone.short_description = 'Phone'  # 指定 'Phone' 給 phone 方法的 short_description
    joined_date.short_description = 'Joined Date'  # 指定 'Joined Date' 給 joined_date 方法的 short_description
# Register your models here.
admin.site.register(Member, MemberAdmin)

