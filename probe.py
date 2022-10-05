def foo(x):
    if x == 0:
        print(x)
    else:

        foo(x - 1)
    print(x - 1)


foo(3)
