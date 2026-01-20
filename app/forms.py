from django import forms
from .models import (
    Announcement,
    AnnouncementComment,
    ClassSchedule,
    Event,
    ContactMessage,
    Resource,
    FAQ,
)


# =========================
# ANNOUNCEMENTS
# =========================
class AnnouncementForm(forms.ModelForm):
    class Meta:
        model = Announcement
        fields = ["title", "content"]


class AnnouncementCommentForm(forms.ModelForm):
    class Meta:
        model = AnnouncementComment
        fields = ["text"]
        widgets = {
            "text": forms.Textarea(attrs={"rows": 2, "placeholder": "Write a comment..."})
        }


# =========================
# SCHEDULES
# =========================
class ClassScheduleForm(forms.ModelForm):
    class Meta:
        model = ClassSchedule
        fields = ["class_name", "course", "section", "day", "time", "instructor_name"]


# =========================
# EVENTS
# =========================
class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ["event_title", "event_description", "event_date", "location"]


# =========================
# CONTACT
# =========================
class ContactMessageForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ["name", "email", "subject", "message"]


# =========================
# RESOURCES
# =========================
class ResourceForm(forms.ModelForm):
    class Meta:
        model = Resource
        fields = ["title", "description", "link"]


# =========================
# FAQS
# =========================
class FAQForm(forms.ModelForm):
    class Meta:
        model = FAQ
        fields = ["question", "answer"]
