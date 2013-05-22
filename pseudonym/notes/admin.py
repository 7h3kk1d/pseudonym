from django.contrib import admin
from notes.models import Note


class NoteAdmin(admin.ModelAdmin):
    list_display = ('id', 'text', 'pub_date', 'author')
admin.site.register(Note, NoteAdmin)
