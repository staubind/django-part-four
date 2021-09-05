from django import template

# get access to a register object which we'll need to register our new filter.
register = template.Library()

# value in a template filter will always be the var passed from context (i.e. {{ var_name|filter:"param"}})
# in this case, cut is filter, var_name is whatever we call this on in teh template, and param is arg
# def cut(value, arg):
#     """
#     This cuts out all values of "arg" from the string!
#     """
#     return value.replace(arg,'') # replace is a string func, so we're assuming value is a string
    # so this would replace the instances of arg within value with ''

# now to register the filter
# filter takes two arguments
    # a string which is how you'll actually call it in the template,
    # and the function as defined in this file
# register.filter('cutt', cut) # see index.html, we call {{ text|cutt:"hello"}}

# or we can use decorators, like so:
@register.filter(name='cutt') # name is cutt, or whatever we want to use, and it takes in function cut
def cut(value, arg):
    """
    This cuts out all values of "arg" from the string!
    """
    return value.replace(arg,'') 