from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse
from django.views.generic import CreateView

from posts.forms import PostForm
from posts.models import Post


class CreateView(LoginRequiredMixin, CreateView):
    template_name = 'posts/create.html'
    form_class = PostForm
    model = Post


    def get_success_url(self):
        return reverse('index')
        # return reverse('post', kwargs={'pk': self.object.pk})