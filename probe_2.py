
def handler(_func):
    def wrapper(func):
        def sub_wrapper(*args, **kwargs):
            print(*args)
            print(**kwargs)
            return func(*args, **kwargs)
        return sub_wrapper
    return wrapper


@handler
def my_func(text):
    if text.text == 'hello':
        print(text)
    else:
        print(False)


my_text = 'hello'

my_func(my_text)
