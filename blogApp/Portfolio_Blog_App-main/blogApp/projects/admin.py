from django.contrib import admin
from projects.models import Projects

class Project_Info(admin.ModelAdmin):
    pass

admin.site.register(Projects, Project_Info)