from django.urls import path
from django.views.generic import TemplateView
from .views import add_announcement_comment

from .views import (
    # public pages
    HomePageView, SchedulesPageView, EventsPageView, ContactPageView,
    ResourceListView, ResourceDetailView,
    FAQListView, FAQDetailView,

    # auth
    StudentHubLoginView, StudentHubLogoutView, SignupView,

    # staff-only (CRUD)
    AnnouncementDetailView, AnnouncementCreateView, AnnouncementUpdateView, AnnouncementDeleteView,
    ScheduleCreateView, ScheduleUpdateView, ScheduleDeleteView,
    EventCreateView, EventUpdateView, EventDeleteView,
    ResourceCreateView, ResourceUpdateView, ResourceDeleteView,
    FAQCreateView, FAQUpdateView, FAQDeleteView,
    ContactMessagesListView,


    # likes
    toggle_announcement_like,


)

urlpatterns = [
    # ---------- AUTH ----------
    path("login/", StudentHubLoginView.as_view(), name="login"),
    path("logout/", StudentHubLogoutView.as_view(), name="logout"),
    path("signup/", SignupView.as_view(), name="signup"),
    path("logged-out/", TemplateView.as_view(template_name="auth/logged_out.html"), name="logged_out"),

    # ---------- PUBLIC PAGES ----------
    path("", HomePageView.as_view(), name="home"),
    path("schedules/", SchedulesPageView.as_view(), name="schedules"),
    path("events/", EventsPageView.as_view(), name="events"),
    path("resources/", ResourceListView.as_view(), name="resources"),
    path("faqs/", FAQListView.as_view(), name="faqs"),
    path("contact/", ContactPageView.as_view(), name="contact"),

    # ---------- ANNOUNCEMENTS ----------
    path("announcements/<int:pk>/", AnnouncementDetailView.as_view(), name="announcement_detail"),
    path("announcements/new/", AnnouncementCreateView.as_view(), name="announcement_create"),
    path("announcements/<int:pk>/edit/", AnnouncementUpdateView.as_view(), name="announcement_update"),
    path("announcements/<int:pk>/delete/", AnnouncementDeleteView.as_view(), name="announcement_delete"),
    path("announcements/<int:pk>/like/", toggle_announcement_like, name="announcement_like"),

    # ---------- SCHEDULES CRUD ----------
    path("schedules/new/", ScheduleCreateView.as_view(), name="schedule_create"),
    path("schedules/<int:pk>/edit/", ScheduleUpdateView.as_view(), name="schedule_update"),
    path("schedules/<int:pk>/delete/", ScheduleDeleteView.as_view(), name="schedule_delete"),

    # ---------- EVENTS CRUD ----------
    path("events/new/", EventCreateView.as_view(), name="event_create"),
    path("events/<int:pk>/edit/", EventUpdateView.as_view(), name="event_update"),
    path("events/<int:pk>/delete/", EventDeleteView.as_view(), name="event_delete"),

    # ---------- RESOURCES ----------
    path("resources/new/", ResourceCreateView.as_view(), name="resource_create"),
    path("resources/<int:pk>/", ResourceDetailView.as_view(), name="resource_detail"),
    path("resources/<int:pk>/edit/", ResourceUpdateView.as_view(), name="resource_update"),
    path("resources/<int:pk>/delete/", ResourceDeleteView.as_view(), name="resource_delete"),

    # ---------- FAQS ----------
    path("faqs/new/", FAQCreateView.as_view(), name="faq_create"),
    path("faqs/<int:pk>/", FAQDetailView.as_view(), name="faq_detail"),
    path("faqs/<int:pk>/edit/", FAQUpdateView.as_view(), name="faq_update"),
    path("faqs/<int:pk>/delete/", FAQDeleteView.as_view(), name="faq_delete"),

    # ---------- STAFF MESSAGES ----------
    path("contact/messages/", ContactMessagesListView.as_view(), name="contact_messages"),
    path("announcements/<int:pk>/like/", toggle_announcement_like, name="announcement_like"),
    path("announcements/<int:pk>/comment/", add_announcement_comment, name="announcement_comment"),

]
