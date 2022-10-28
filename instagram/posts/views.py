from django.contrib.auth.mixins import LoginRequiredMixin

from django.views.generic import ListView

from posts.models import Post


class IndexView(LoginRequiredMixin, ListView):
    login_url = 'accounts/login/'
    redirect_field_name = 'redirect_to'
    template_name = 'index.html'
    model = Post
    context_object_name = 'posts'

