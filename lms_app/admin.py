from django.contrib import admin
from .models import (
    Profile,
    Section,
    Question,
    Answer,
    Grade
)
admin.site.register(Profile)
admin.site.register(Section)
admin.site.register(Question)
admin.site.register(Answer)
admin.site.register(Grade)
