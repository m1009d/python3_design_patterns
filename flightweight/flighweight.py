"""Flight-weight python design pattern.

Example was ispired by the book: Mastering Python Design Patterns (Sakis Kasampalis) 2015, Packt Publishing.
"""

from enum import Enum
import random


BerryType = Enum('Berry', 'strawberry raspberry')


class Berry:

    berry_type: BerryType
    pool = {}

    def __new__(cls, berry_type: BerryType):
        obj = cls.pool.get(berry_type)
        if obj is None:
            obj = object.__new__(cls)
            cls.pool[berry_type] = obj
            obj.__setattr__('berry_type', berry_type)
        return obj

    def render(self, x: int, y: int) -> None:
        print(f'rendering {self.berry_type} at ({x}:{y})')


def main() -> int:

    min_point, max_point = 0, 200
    berry_counter = 0

    for _ in range(7):
        t1 = Berry(BerryType.strawberry)
        t1.render(x=random.randint(min_point, max_point),
                  y=random.randint(min_point, max_point))

        berry_counter += 1

    for _ in range(4):
        t2 = Berry(BerryType.raspberry)
        t2.render(x=random.randint(min_point, max_point),
                  y=random.randint(min_point, max_point))

        berry_counter += 1

    print(f'Berries rendered: {berry_counter}')
    print(f'Berries actually created: {len(Berry.pool)}')

    return 0


if __name__ == '__main__':
    raise SystemExit(main())
