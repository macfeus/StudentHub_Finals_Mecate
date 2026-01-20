from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.db.models import Q
from .models import AnnouncementLike, AnnouncementComment
from .forms import AnnouncementCommentForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import (
    ListView, DetailView, TemplateView
)
from django.views.generic.edit import (
    CreateView, UpdateView, DeleteView, FormView
)
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.views import View

from .models import (
    Announcement, ClassSchedule, Event,
    ContactMessage, Resource, FAQ, AnnouncementLike
)
from .forms import (
    AnnouncementForm, ClassScheduleForm, EventForm,
    ContactMessageForm, ResourceForm, FAQForm

)

# ==============================
# STAFF-ONLY MIXIN
# ==============================
class StaffRequiredMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_staff


# ==============================
# AUTH
# ==============================
class StudentHubLoginView(LoginView):
    template_name = "auth/login.html"
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy("home")


class StudentHubLogoutView(LogoutView):
    next_page = reverse_lazy("logged_out")


class SignupView(FormView):
    template_name = "auth/signup.html"
    form_class = UserCreationForm
    success_url = reverse_lazy("home")

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return super().form_valid(form)


class LoggedOutLandingView(TemplateView):
    template_name = "auth/logged_out.html"


# ==============================
# PUBLIC PAGES
# ==============================
class HomePageView(ListView):
    model = Announcement
    template_name = "app/home.html"
    context_object_name = "announcements"
    paginate_by = 5

    def get_queryset(self):
        qs = Announcement.objects.select_related("posted_by").order_by("-date_posted")
        q = self.request.GET.get("q")
        if q:
            qs = qs.filter(Q(title__icontains=q) | Q(content__icontains=q))
        return qs


class SchedulesPageView(ListView):
    model = ClassSchedule
    template_name = "app/schedules.html"
    context_object_name = "schedules"


class EventsPageView(ListView):
    model = Event
    template_name = "app/events.html"
    context_object_name = "events"


class ResourceListView(ListView):
    model = Resource
    template_name = "app/resources.html"
    context_object_name = "resources"


class FAQListView(ListView):
    model = FAQ
    template_name = "app/faqs.html"
    context_object_name = "faqs"


class ContactPageView(FormView):
    template_name = "app/contact.html"
    form_class = ContactMessageForm
    success_url = reverse_lazy("contact")

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


# ==============================
# ANNOUNCEMENT DETAIL
# ==============================
class AnnouncementDetailView(DetailView):
    model = Announcement
    template_name = "announcements/detail.html"
    context_object_name = "announcement"


# ==============================
# LIKE TOGGLE
# ==============================
@login_required
def toggle_announcement_like(request, pk):
    announcement = get_object_or_404(Announcement, pk=pk)

    like, created = AnnouncementLike.objects.get_or_create(
        announcement=announcement,
        user=request.user
    )

    if not created:
        like.delete()

    return redirect(request.META.get("HTTP_REFERER", "home"))


# ==============================
# STAFF-ONLY CRUD
# ==============================
class AnnouncementCreateView(LoginRequiredMixin, StaffRequiredMixin, CreateView):
    model = Announcement
    form_class = AnnouncementForm
    template_name = "announcements/form.html"
    success_url = reverse_lazy("home")

    def form_valid(self, form):
        form.instance.posted_by = self.request.user
        return super().form_valid(form)


class AnnouncementUpdateView(LoginRequiredMixin, StaffRequiredMixin, UpdateView):
    model = Announcement
    form_class = AnnouncementForm
    template_name = "announcements/form.html"
    success_url = reverse_lazy("home")


class AnnouncementDeleteView(LoginRequiredMixin, StaffRequiredMixin, DeleteView):
    model = Announcement
    template_name = "announcements/delete.html"
    success_url = reverse_lazy("home")

# ==============================
# STAFF-ONLY CRUD: SCHEDULES
# ==============================
class ScheduleCreateView(LoginRequiredMixin, StaffRequiredMixin, CreateView):
    model = ClassSchedule
    form_class = ClassScheduleForm
    template_name = "schedules/form.html"
    success_url = reverse_lazy("schedules")

    def form_valid(self, form):
        form.instance.instructor = self.request.user
        return super().form_valid(form)


class ScheduleUpdateView(LoginRequiredMixin, StaffRequiredMixin, UpdateView):
    model = ClassSchedule
    form_class = ClassScheduleForm
    template_name = "schedules/form.html"
    success_url = reverse_lazy("schedules")


class ScheduleDeleteView(LoginRequiredMixin, StaffRequiredMixin, DeleteView):
    model = ClassSchedule
    template_name = "schedules/delete.html"
    success_url = reverse_lazy("schedules")


# ==============================
# STAFF-ONLY CRUD: EVENTS
# ==============================
class EventCreateView(LoginRequiredMixin, StaffRequiredMixin, CreateView):
    model = Event
    form_class = EventForm
    template_name = "events/form.html"
    success_url = reverse_lazy("events")

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)


class EventUpdateView(LoginRequiredMixin, StaffRequiredMixin, UpdateView):
    model = Event
    form_class = EventForm
    template_name = "events/form.html"
    success_url = reverse_lazy("events")


class EventDeleteView(LoginRequiredMixin, StaffRequiredMixin, DeleteView):
    model = Event
    template_name = "events/delete.html"
    success_url = reverse_lazy("events")


# ==============================
# STAFF-ONLY CRUD: RESOURCES
# ==============================
class ResourceDetailView(DetailView):
    model = Resource
    template_name = "resources/detail.html"
    context_object_name = "resource"


class ResourceCreateView(LoginRequiredMixin, StaffRequiredMixin, CreateView):
    model = Resource
    form_class = ResourceForm
    template_name = "resources/form.html"
    success_url = reverse_lazy("resources")

    def form_valid(self, form):
        form.instance.uploaded_by = self.request.user
        return super().form_valid(form)


class ResourceUpdateView(LoginRequiredMixin, StaffRequiredMixin, UpdateView):
    model = Resource
    form_class = ResourceForm
    template_name = "resources/form.html"
    success_url = reverse_lazy("resources")


class ResourceDeleteView(LoginRequiredMixin, StaffRequiredMixin, DeleteView):
    model = Resource
    template_name = "resources/delete.html"
    success_url = reverse_lazy("resources")


# ==============================
# STAFF-ONLY CRUD: FAQS
# ==============================
class FAQDetailView(DetailView):
    model = FAQ
    template_name = "faqs/detail.html"
    context_object_name = "faq"


class FAQCreateView(LoginRequiredMixin, StaffRequiredMixin, CreateView):
    model = FAQ
    form_class = FAQForm
    template_name = "faqs/form.html"
    success_url = reverse_lazy("faqs")

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)


class FAQUpdateView(LoginRequiredMixin, StaffRequiredMixin, UpdateView):
    model = FAQ
    form_class = FAQForm
    template_name = "faqs/form.html"
    success_url = reverse_lazy("faqs")


class FAQDeleteView(LoginRequiredMixin, StaffRequiredMixin, DeleteView):
    model = FAQ
    template_name = "faqs/delete.html"
    success_url = reverse_lazy("faqs")


class ContactMessagesListView(LoginRequiredMixin, StaffRequiredMixin, ListView):
    model = ContactMessage
    template_name = "contacts/message_list.html"
    context_object_name = "messages"
    paginate_by = 10


@login_required
def toggle_announcement_like(request, pk):
    announcement = get_object_or_404(Announcement, pk=pk)

    like, created = AnnouncementLike.objects.get_or_create(
        announcement=announcement,
        user=request.user
    )

    if not created:
        like.delete()

    return redirect(request.POST.get("next", "home"))


@login_required
def add_announcement_comment(request, pk):
    announcement = get_object_or_404(Announcement, pk=pk)

    if request.method == "POST":
        form = AnnouncementCommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.announcement = announcement
            comment.user = request.user
            comment.save()

    return redirect(request.POST.get("next", "home"))
from .models import AnnouncementComment  # add this import
from .forms import AnnouncementCommentForm  # add this import (we'll create it)

@login_required
def add_announcement_comment(request, pk):
    announcement = get_object_or_404(Announcement, pk=pk)

    if request.method == "POST":
        form = AnnouncementCommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.announcement = announcement
            comment.user = request.user
            comment.save()

    return redirect(request.META.get("HTTP_REFERER", "home"))


class ScheduleCreateView(LoginRequiredMixin, StaffRequiredMixin, CreateView):
    model = ClassSchedule
    form_class = ClassScheduleForm
    template_name = "schedules/form.html"
    success_url = reverse_lazy("schedules")

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)
