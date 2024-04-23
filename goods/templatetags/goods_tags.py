from django import template
<<<<<<< HEAD
from django.utils.http import urlencode

=======
>>>>>>> 7203c0d3ca24d97ad35e4406b64f3838b5a5f355

from goods.models import Categories


register = template.Library()


@register.simple_tag
def tag_categories():
<<<<<<< HEAD
    return Categories.objects.all()



@register.simple_tag(takes_context=True)
def changes_params(context,**kwargs):
    query = context['request'].GET.dict()
    query.update(kwargs)
    return urlencode(query)
=======
    return Categories.objects.all()
>>>>>>> 7203c0d3ca24d97ad35e4406b64f3838b5a5f355
