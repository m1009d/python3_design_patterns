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


class ToyFactory(ABC):

    @abstractmethod
    def create(self, name: str) -> None:
        ...


class DuckToy(ToyFactory):

    def create(self, name: str) -> None:
        duckmold = DuckMold()
        duckmold.inject(name)


class CarToy(ToyFactory):

    def create(self, name: str) -> None:
        duckmold = DuckMold()
        duckmold.inject(name)


def main() -> int:

    duck_toy= DuckToy()
    car_toy = CarToy()

    duck_toy.create('duck1')
    car_toy.create('car1')

    return 0


if __name__ == "__main__":

    raise SystemExit(main())
