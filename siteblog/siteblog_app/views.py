from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post, Category, Tag


class HomeView(ListView):
    model = Post
    template_name = 'siteblog_app/index.html'
    context_object_name = 'posts'
    ordering = ['-created_at']
    paginate_by = 3

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Home'
        return context


def index(request):
    return render(request, 'siteblog_app/index.html')

def get_category(request, slug):
    return render(request, 'siteblog_app/category.html')

def get_post(request, slug):
    return render(request, 'siteblog_app/category.html')
