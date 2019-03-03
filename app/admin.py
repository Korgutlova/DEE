from django.contrib import admin

from app.models import Competence, Module, Student, Role, Interest, Evaluation, Content, StudentCompetence

admin.site.register(Competence)
admin.site.register(Module)
admin.site.register(Student)
admin.site.register(Role)
admin.site.register(Interest)
admin.site.register(Evaluation)
admin.site.register(Content)
admin.site.register(StudentCompetence)
