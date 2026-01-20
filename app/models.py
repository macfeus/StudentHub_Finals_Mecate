from django.db import models
from django.conf import settings


# ==========================
# ANNOUNCEMENTS
# ==========================
class Announcement(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)
    posted_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.title


class AnnouncementLike(models.Model):
    announcement = models.ForeignKey(
        Announcement,
        on_delete=models.CASCADE,
        related_name="likes"
    )
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="announcement_likes"
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ("announcement", "user")

    def __str__(self):
        return f"{self.user} liked {self.announcement}"


class AnnouncementComment(models.Model):
    announcement = models.ForeignKey(
        Announcement,
        on_delete=models.CASCADE,
        related_name="comments"
    )
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="announcement_comments"
    )
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.user} commented on {self.announcement}"


# ==========================
# CLASS SCHEDULES
# ==========================
class ClassSchedule(models.Model):
    DAYS = [
        ("Mon", "Monday"),
        ("Tue", "Tuesday"),
        ("Wed", "Wednesday"),
        ("Thu", "Thursday"),
        ("Fri", "Friday"),
        ("Sat", "Saturday"),
        ("Sun", "Sunday"),
    ]

    COURSES = [
        ("CRIM", "Criminology"),
        ("PSY", "Psychology"),
        ("CS", "Computer Science"),
        ("EDUC", "Education"),
        ("HM", "Hospitality Management"),
        ("IT", "Information Technology"),
    ]

    class_name = models.CharField(max_length=100)
    course = models.CharField(
        max_length=10,
        choices=COURSES,
        default="IT"
    )
    section = models.CharField(
        max_length=50,
        default="A"
    )
    day = models.CharField(
        max_length=10,
        choices=DAYS
    )
    time = models.TimeField()
    instructor_name = models.CharField(
        max_length=120,
        default="TBA"
    )

    def __str__(self):
        return f"{self.class_name} - {self.get_course_display()} ({self.section})"


# ==========================
# EVENTS
# ==========================
class Event(models.Model):
    event_title = models.CharField(max_length=255)
    event_description = models.TextField()
    event_date = models.DateTimeField()
    location = models.CharField(max_length=100)
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.event_title


# ==========================
# CONTACT MESSAGES
# ==========================
class ContactMessage(models.Model):
    name = models.CharField(max_length=120)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.subject} - {self.email}"


# ==========================
# RESOURCES
# ==========================
class Resource(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    link = models.URLField(blank=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    uploaded_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.title


# ==========================
# FAQS
# ==========================
class FAQ(models.Model):
    question = models.CharField(max_length=255)
    answer = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.question
