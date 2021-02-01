from django.template import Library

register = Library()

@register.filter
def rangess(start, number):
    return range(start, number)


@register.filter
def slice_function(function_list, index_number):
    print(function_list, index_number)
    print(function_list[index_number])
    return function_list[index_number]