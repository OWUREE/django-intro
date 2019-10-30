from django import template

register = template.Library()


@register.filter
def add_class(form_input, css_class):
    return form_input.as_widget(attrs={'class': css_class})