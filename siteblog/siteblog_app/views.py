from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post, Category, Tag
from django.db.models import F


class HomeView(ListView):
    model = Post
    template_name = 'siteblog_app/index.html'
    context_object_name = 'posts'
    ordering = ['-created_at']
    paginate_by = 3

    def get_queryset(self):
        return Post.objects.filter(guide=False)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Статьи по программированию и технологиям разработки ПО'
        context['meta_description'] = 'Блог о программировании и технологиях разработки программного обеспечения'
        context['meta_keywords'] = 'программирование, разработка ПО, технологии, IT'
        return context


class PostsByCategory(ListView):
    template_name = 'siteblog_app/guide.html'
    context_object_name = 'posts'
    paginate_by = 10
    #allow_empty = False

    def get_queryset(self):
        return Post.objects.filter(category__slug=self.kwargs['slug'], guide=True).order_by('created_at')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        category = Category.objects.get(slug=self.kwargs['slug'])
        context['title'] = category.title
        context['text'] = 'и его особенности' if self.get_queryset().exists() and self.get_queryset()[
            0].guide and category.id <= 3 else 'в разработке ПО'
        context['meta_description'] = category.description
        context['meta_keywords'] = category.keywords
        return context


class PostsByTag(ListView):
    template_name = 'siteblog_app/index.html'
    context_object_name = 'posts'
    paginate_by = 3
    #allow_empty = False

    def get_queryset(self):
        return Post.objects.filter(tags__slug=self.kwargs['slug'])

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        tag = Tag.objects.get(slug=self.kwargs['slug'])
        context['title'] = 'Статьи по тегу #' + str(tag)
        context['meta_description'] = tag.description
        context['meta_keywords'] = tag.keywords
        return context


class GetPost(DetailView):
    model = Post
    template_name = 'siteblog_app/post.html'
    context_object_name = 'post'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        self.object.count_views = F('count_views') + 1
        self.object.save()
        self.object.refresh_from_db()
        context['meta_description'] = self.object.description
        context['meta_keywords'] = self.object.keywords
        return context


class Search(ListView):
    template_name = 'siteblog_app/search.html'
    context_object_name = 'posts'
    paginate_by = 3

    def get_queryset(self):
        return Post.objects.filter(title__icontains=self.request.GET.get('s'))

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        search_query = self.request.GET.get('s')
        context['srch'] = f"{search_query}"
        context['s'] = f"s={search_query}&"
        context['title'] = f'Результаты поиска "{search_query}"'
        context['meta_description'] = f'Результаты поиска по запросу: {search_query}'
        context['meta_keywords'] = f'поиск, {search_query}'
        return context

def page_not_found(request, exception):
    context = {
        'title': 'Страница не найдена (404)',
        'meta_description': 'Запрашиваемая страница не существует или была перемещена',
        'meta_keywords': '404, страница не найдена'
    }
    return render(request, '404.html', context=context, status=404)
