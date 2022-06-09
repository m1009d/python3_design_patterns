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


class Duck(Mold):

    def inject(self, name: str) -> None:
        print(f'Making {name} from duck mold')


class Car(Mold):

    def inject(self, name: str) -> None:
        print(f'Making {name} from car mold')


class ToyFactory:

    def __init__(self, kind: Mold) -> None:
        self.kind = kind

    def create(self, name: str) -> None:
        self.kind.inject(name)


def main() -> int:

    duck = Duck()
    car = Car()
    duck_toy = ToyFactory(duck)
    duck_toy.create('duck1')

    car_toy = ToyFactory(car)
    car_toy.create('car1')

    return 0


if __name__ == "__main__":

    raise SystemExit(main())
