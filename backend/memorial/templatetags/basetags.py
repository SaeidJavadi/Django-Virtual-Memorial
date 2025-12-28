from django import template

register = template.Library()


@register.filter()
def even_test(value):
    print(value)
    if value+1 / 2 == 0:
        print('ok')
        return True
    else:
        print('nk')
        return False

@register.filter()
def deadActive(value):
    c = value.filter(status='active').all().count()
    return c