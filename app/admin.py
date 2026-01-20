from django.contrib import admin
from .models import (
    Announcement,
    AnnouncementLike,
    AnnouncementComment,
    ClassSchedule,
    Event,
    ContactMessage,
    Resource,
    FAQ,
)

admin.site.register(Announcement)
admin.site.register(AnnouncementLike)
admin.site.register(AnnouncementComment)
admin.site.register(ClassSchedule)
admin.site.register(Event)
admin.site.register(ContactMessage)
admin.site.register(Resource)
admin.site.register(FAQ)



