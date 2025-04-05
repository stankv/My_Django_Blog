from django import template
from siteblog_app.models import Post, Tag

register = template.Library()

@register.inclusion_tag('siteblog_app/popular_posts_tpl.html')
def get_popular_posts(cnt=3):    # кол-во выводимых постов
    posts = Post.objects.order_by('-count_views')[:cnt]
    return {"posts": posts}

