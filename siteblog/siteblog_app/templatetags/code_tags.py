# В code_tags.py
import re
from django import template
from django.utils.safestring import mark_safe

register = template.Library()

@register.filter
def parse_custom_code_blocks(value):
    """Парсит кастомные теги <my_code> в HTML для подсветки"""
    pattern = r'<my_code class="language-([^"]+)">(.*?)</my_code>'
    # pattern = r'<p>\s*<my_code class="language-([^"]+)">(.*?)</my_code>\s*</p>'

    def replace_code(match):
        language = match.group(1)
        code = match.group(2).strip()
        return f'<div class="md-code-block md-code-block-light"><pre><button class="copy-code" title="Копировать код"><svg viewBox="0 0 24 24"><path d="M19,21H8V7H19M19,5H8A2,2 0 0,0 6,7V21A2,2 0 0,0 8,23H19A2,2 0 0,0 21,21V7A2,2 0 0,0 19,5M16,1H4A2,2 0 0,0 2,3V17H4V3H16V1Z"/></svg></button><code class="language-{language}">{code}</code></pre></div>'

    return mark_safe(re.sub(pattern, replace_code, value, flags=re.DOTALL))
