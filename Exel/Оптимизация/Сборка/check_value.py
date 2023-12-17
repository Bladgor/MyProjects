def check_value(my_value):
    try:
        int(my_value)
        return True
    except ValueError:
        return False
