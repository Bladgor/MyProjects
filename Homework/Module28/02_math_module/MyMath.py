
import math
from typing import Union


class MyMath:

    @classmethod
    def circle_len(cls, radius: int) -> Union[int, float]:
        return 2 * math.pi * radius

    @classmethod
    def circle_sq(cls, radius: int) -> Union[int, float]:
        return math.pi * radius ** 2

    @classmethod
    def cube_volume(cls, len_a: int) -> Union[int, float]:
        return len_a ** 3

    @classmethod
    def sphere_sq(cls, radius: int) -> Union[int, float]:
        return 4 * math.pi * radius ** 2
