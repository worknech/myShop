from django import template
from django.utils.http import urlencode

from goods.models import Categories


register = template.Library()


@register.simple_tag()
def tag_categories():
    """
    Пользовательский тег Django для получения всех категорий из модели `Categories`.

    Возвращает:
        QuerySet: Все объекты модели `Categories`, загруженные из базы данных.

    Использование в шаблоне:
        {% load your_template_tags %}
        {% for category in tag_categories %}
            {{ category.name }}
        {% endfor %}

    Примечание:
        - Модель `Categories` должна быть определена и импортирована.
        - Тег необходимо зарегистрировать в файле с пользовательскими тегами.
        - Для использования в шаблоне требуется предварительная загрузка тега через `{% load %}`.
    """
    return Categories.objects.all()


@register.simple_tag(takes_context=True)
def change_params(context, **kwargs):
    query = context['request'].GET.dict()
    query.update(kwargs)
    return urlencode(query)