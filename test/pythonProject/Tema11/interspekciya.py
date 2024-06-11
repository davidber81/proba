import inspect

# def introspection_info(obj):
#    print(obj)
#
# number_info = introspection_info(42)
# print(number_info)
# print(type(number_info))
# print(dir(number_info))
# print(hasattr(number_info, 'get'))
# print(classmethod(number_info))
# print(__name__)
# print(inspect.ismodule(number_info))
# print(inspect.isclass(number_info))
# print(inspect.isfunction(number_info))
# print(inspect.isbuiltin(number_info))
#
# signature = inspect.signature(introspection_info)
# print(type(signature), signature)
# print(dir(signature))


def introspection_info(obj):
   print(obj)
   my_dict = {'type': type(obj), 'dir': dir(obj), 'hasattr': hasattr(obj, 'get'), 'classmethod': classmethod(obj),
              'name': __name__, 'module': inspect.ismodule(obj), 'class': inspect.isclass(obj),
              'function': inspect.isfunction(obj), 'builtin': inspect.isbuiltin(obj)}

   return my_dict
number_info = introspection_info(42)
print(number_info)