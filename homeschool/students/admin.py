from django.contrib import admin

from homeschool.students.models import Coursework, Student


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ("id", "school", "first_name", "last_name")
    raw_id_fields = ("school",)


@admin.register(Coursework)
class CourseworkAdmin(admin.ModelAdmin):
    list_display = ("id", "course_task", "completed_date")
    raw_id_fields = ("course_task",)
