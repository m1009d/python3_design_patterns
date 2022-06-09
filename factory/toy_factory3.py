#!/usr/bin/env python3

"""Factory pattern.

The factory pattern defines an interface for creating an object, but let's
subclasses decide which class to instantiate.
Factory methods let a class defer instantiation to subclasses.
"""

from abc import ABC, abstractmethod

class Mold(ABC):

    @abstractmethod
    def inject(self, name: str) -> None:
        ...


class DuckMold(Mold):
    def inject(self, name: str) -> None:
        print(f'Making {name} from duck mold')


class CarMold(Mold):
    def inject(self, name: str) -> None:
        print(f'Making {name} from car mold')


def create_toy(name: str) -> Mold:
    """Factory function."""

    if name.lower() == 'duck':
        duck = DuckMold()
        duck.inject(name)
        return duck

    if name.lower() == 'car':
        car = CarMold()
        car.inject(name)
        return car

    raise AssertionError(f"I don't know how to make {name!r}")


def main() -> None:
    create_toy('duck')
    create_toy('car')


if __name__ == "__main__":

    main()
