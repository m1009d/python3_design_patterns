#!/usr/bin/env python3

# pylint: disable=missing-class-docstring,missing-function-docstring


"""Factory pattern.

The factory pattern defines an interface for creating an object, but let's
subclasses decide which class to instantiate.
Factory methods let a class defer instantiation to subclasses.

Thanks to Be A Better Dev channel:
https://www.youtube.com/watch?v=TdJatgto5cU
"""

from abc import ABC, abstractmethod



class Pizza(ABC):
    """Abstract class for Pizza."""

    @abstractmethod
    def prepare(self):
        """Abstract method to create a pizza."""

    @abstractmethod
    def bake(self):
        """Abstract method to bake a pizza."""

    @abstractmethod
    def cut(self):
        """Abstract method to cut a pizza."""

    @abstractmethod
    def box(self):
        """Abstract method to box a pizza."""


class CheesePizza(Pizza):
    """Cheese pizza class."""

    def prepare(self) -> None:
        """Prepare Cheese pizza."""
        print('Creating Cheese Pizza')

    def bake(self) -> None:
        """Bake Cheese pizza."""
        print('Baking Cheese Pizza')

    def cut(self) -> None:
        """Cut Cheese pizza."""
        print('Cutting Cheese Pizza')

    def box(self) -> None:
        """Box Cheese pizza."""
        print('Boxing Cheese Pizza')


class HawaiPizza(Pizza):
    """Hawai pizza class."""

    def prepare(self) -> None:
        """Prepare Hawai pizza."""
        print('Creating Hawai Pizza')

    def bake(self) -> None:
        """Bake Hawai pizza."""
        print('Baking Hawai Pizza')

    def cut(self) -> None:
        """Cut Hawai pizza."""
        print('Cutting Hawai Pizza')

    def box(self) -> None:
        """Box Hawai pizza."""
        print('Boxing Hawai Pizza')



class PizzaFactory(ABC):
    """Abstract factory class.

    This class is responsible just for defining an interface.
    Subclasses decide which class to instantiate.
    """

    @abstractmethod
    def create(self):
        """Abstract method to create a specific pizza type."""


class CheesePizzaFactory(PizzaFactory):
    """Factory subclass instantiating the CheesePizza class."""

    def create(self) -> CheesePizza:
        """Create the cheese pizza."""
        pizza = CheesePizza()
        pizza.prepare()
        pizza.bake()
        pizza.cut()
        pizza.box()
        return pizza


class HawaiPizzaFactory(PizzaFactory):
    """Factory subclass instantiating the HawaiPizza class."""

    def create(self) -> HawaiPizza:
        """Create the hawai pizza."""
        pizza = HawaiPizza()
        pizza.prepare()
        pizza.bake()
        pizza.cut()
        pizza.box()
        return pizza


def order_pizza() -> PizzaFactory:
    """Ask user which pizza to create and return the factory subclass."""
    pizza_map = {
        '1': CheesePizzaFactory(),
        '2': HawaiPizzaFactory()
    }

    while True:
        answer = input('''
            Select pizza:
                1 - Cheese
                2 - Hawai

            : ''')
        if answer in pizza_map:
            return pizza_map[answer]
        print('{answer!r} is not a valid option!')


def main(pizza: PizzaFactory) -> None:
    """Let's create the chosen pizza."""
    pizza.create()


if __name__ == "__main__":

    main(order_pizza())
