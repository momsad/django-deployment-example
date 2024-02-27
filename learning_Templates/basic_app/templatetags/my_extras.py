from django import template


register = template.library()

@register.filter(name='cut')
def cut(value,arg):
    """
    this cuts all value of 'arg' fm the string!
    """
    return

 
# register.filter('cut',cut)