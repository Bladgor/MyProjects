from functools import reduce
import operator


class Calculator:

    def summation(self, *args):
        return sum(list(args))

    def subtraction(self, *args):
        return reduce(operator.__sub__, (list(args)))

    def multiplication(self, *args):
        return reduce(operator.__mul__, list(args))

    def division(self, *args):
        try:
            result = reduce(operator.__truediv__, list(args))
            if result % round(result) == 0:
                return round(result)
            return result
        except ZeroDivisionError:
            return 'На ноль делить нельзя!'

    def power(self, *args):
        return reduce(operator.__pow__, list(args))


calculator = Calculator()
