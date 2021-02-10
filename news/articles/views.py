from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

from . import models


class ArticleCreateView(LoginRequiredMixin, CreateView):
    model = models.Article
    template_name = 'article_new.html'
    fields = ['title', 'body', ] 
    login_url = 'login' # new

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class ArticleListView(LoginRequiredMixin, ListView): # update
    model = models.Article
    template_name = 'article_list.html'
    login_url = 'login' # new


class ArticleDetailView(LoginRequiredMixin, DetailView): # update
    model = models.Article
    template_name = 'article_detail.html'
    login_url = 'login' # new


class ArticleUpdateView(LoginRequiredMixin, UpdateView): # update
    model = models.Article
    fields = ['title', 'body', ]
    template_name = 'article_edit.html'
    login_url = 'login' # new


class ArticleDeleteView(LoginRequiredMixin, DeleteView): # update
    model = models.Article
    template_name = 'article_delete.html'
    success_url = reverse_lazy('article_list')
    login_url = 'login' # new
