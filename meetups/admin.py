from django.contrib import admin
from .models import Meetup, Location, Participant

# Register your models here.

class MeetupAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'location_of_meetup')
    list_filter = ('location_of_meetup', 'date', )
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Meetup, MeetupAdmin)
admin.site.register(Location)
admin.site.register(Participant)

