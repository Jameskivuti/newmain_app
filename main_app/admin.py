from django.contrib import admin

from main_app.models import Student

# Register your models here.
admin.site.site_header = "Elite group of schools"


class StudentAdmin(admin.ModelAdmin):
    list_display = ["first_name", "last_name", "dob", "kcpe_score", "is_sporty"]
    search_fields = ["first_name", "last_name", "kcpe_score"]
    list_filter = ["is_sporty"]


admin.site.register(Student, StudentAdmin)
