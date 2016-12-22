from django.contrib import admin
from .models import Event


# Register your models here.
class AuthorEvent(admin.ModelAdmin):
    # fields = ('name',)
    list_filter = ('name',)
    list_display = ('name', 'address', 'time')
    actions = ['null_desc']
    search_fields = ('address', )

    def null_desc(self, request, queryset):
        queryset.update(desc=None)


admin.site.register(Event, AuthorEvent)
