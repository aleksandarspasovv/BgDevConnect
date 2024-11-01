from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView, DetailView, ListView


class HomeView(TemplateView):
    template_name = 'index.html'


class LoginView(TemplateView):
    template_name = 'sign-in.html'


class RegisterView(TemplateView):
    template_name = 'sign-up.html'


class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'profile.html'


class ProfileEditView(LoginRequiredMixin, TemplateView):
    template_name = 'profile-edit.html'


class AccountSettingsView(LoginRequiredMixin, TemplateView):
    template_name = 'account-setting.html'


class BlogListView(ListView):
    template_name = 'blog-list.html'
    # model = Blog (Assuming a Blog model)


class BlogDetailView(DetailView):
    template_name = 'blog-detail.html'
    # model = Blog


class StoreView(TemplateView):
    template_name = 'store.html'
