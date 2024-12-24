from django.contrib import admin

# from import_export import ImportExportActionModelAdmin

from .models import SignUp, SignIn, AddJob

@admin.register(SignUp)
class SignUpAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "email")

    search_fields = ("first_name",)
    list_filter = ("first_name",)



@admin.register(SignIn)
class SignInAdmin(admin.ModelAdmin):
    list_display = ("email", "password")
    search_fields = ("email",)
    list_filter = ("email",)


@admin.register(AddJob)
class AddJobAdmin(admin.ModelAdmin):
    list_display = ("title", "company_name", "posted_date")
    search_fields = ("title", "company_name", "description")
    list_filter = ("title", "company_name", "posted_date")

