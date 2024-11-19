from django.contrib import admin

from .models import Board, Label, List, Project, Task

# Register your models here.
admin.site.register(Project)
admin.site.register(Board)
admin.site.register(List)
admin.site.register(Task)
admin.site.register(Label)
