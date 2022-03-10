def my_print(**kwargs):
    print(kwargs.get('param_1'))
    print(kwargs.get('param_2'))
    print(kwargs)


my_print(param_1=123)

