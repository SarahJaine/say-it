from django.contrib import admin
from .models import Example, Musician


def publish(modeladmin, request, queryset):
    queryset.update(status='p')
    publish.short_description = "Publish selected Items"


def retract(modeladmin, request, queryset):
    queryset.update(status='d')
    retract.short_description = "Retract selected Items"


class ExampleAdmin(admin.ModelAdmin):
    model = Example
    list_display = ['title', 'status']
    actions = [publish, retract]


class MusicianAdmin(admin.ModelAdmin):
    model = Musician
    list_display = ['name', 'status']
    actions = [publish, retract]

admin.site.register(Example, ExampleAdmin)
admin.site.register(Musician, MusicianAdmin)
