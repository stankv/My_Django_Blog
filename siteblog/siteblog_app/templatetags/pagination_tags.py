from django import template

register = template.Library()

@register.filter
def add_page_suffix(value, request):
    """Добавляет суффикс с номером страницы для SEO"""
    page_number = request.GET.get('page', '1')
    if page_number != '1':
        return f"{value} - Страница {page_number}"
    return value
