#!/usr/bin/env python3

"""Strategy design pattern.

Try to implement the Duck example from the youtube video:
https://www.youtube.com/watch?v=v9ejT8FO-7I

Other materials used:
https://refactoring.guru/design-patterns/strategy
"""

from abc import ABC, abstractmethod


class IFlyBehavior(ABC):
    """Flying behavior."""

    @abstractmethod
    def fly(self) -> None:
        """Needs to be implemented in the respective Strategy class."""
        return


class IQuackBehavior(ABC):
    """Quack behavior."""

    @abstractmethod
    def quack(self) -> None:
        """Needs to be implemented in the respective Strategy class."""
        return


class SimpleFlyingStrategy(IFlyBehavior):
    """Strategy pattern - inherits from IFlyBehavior."""

    def fly(self) -> str:
        return 'just fly'


class JetFlyingStrategy(IFlyBehavior):
    """Strategy pattern for - inherits from IFlyBehavior."""

    def fly(self) -> str:
        return 'do jet fly'


# Adding a new strategy is simple, we don't need to change
# our Context, Behavior classes or Strategy classes.
class NoFlyingStrategy(IFlyBehavior):
    """Strategy pattern - inherits from IFlyBehavior."""

    def fly(self) -> str:
        return 'not fly'


class SimpleQuackStrategy(IQuackBehavior):
    def quack(self) -> str:
        return 'just quack'


class NoQuackStrategy(IQuackBehavior):
    def quack(self) -> str:
        return 'not quack'


class Duck:
    """
    The original object, called context, holds a reference to a strategy object
    and delegates it executing the behavior.
    """

    def __init__(
        self,
        name: str,
        flying_behaviour: IFlyBehavior,
        quack_behaviour: IQuackBehavior
        ) -> None:
        self.name = name
        self._flying_behaviour = flying_behaviour
        self._quack_behaviour = quack_behaviour

    @property
    def flying_strategy(self) -> IFlyBehavior:
        return self._flying_behaviour

    # able to change the flying_behaviour at runtime
    @flying_strategy.setter
    def flying_strategy(self, flying_behaviour: IFlyBehavior) -> None:
        self._flying_behaviour = flying_behaviour

    @property
    def quack_strategy(self) -> IQuackBehavior:
        return self._quack_behaviour

    # able to change the quack_behaviour at runtime
    @quack_strategy.setter
    def quack_strategy(self, quack_behaviour: IQuackBehavior) -> None:
        self._quack_behaviour = quack_behaviour

    def display(self) -> None:
        print(
            f'{self.name} can {self._flying_behaviour.fly()} '
            f'and can {self._quack_behaviour.quack()}'
        )


if __name__ == "__main__":

    # The client code picks a concrete strategy and passes it to the context.
    # The client should be aware of the differences between strategies in order
    # to make the right choice.
    wild_duck = Duck(name='wild duck', flying_behaviour=SimpleFlyingStrategy(), quack_behaviour=SimpleQuackStrategy())
    cloud_duck = Duck(name='cloud duck', flying_behaviour=JetFlyingStrategy(), quack_behaviour=SimpleQuackStrategy())
    rubber_duck = Duck(name='rubber duck', flying_behaviour=NoFlyingStrategy(), quack_behaviour=NoQuackStrategy())
    wild_duck.display()
    cloud_duck.display()
    rubber_duck.display()

    # We can change the flying behavior at runtime
    wild_duck.flying_strategy = JetFlyingStrategy()
    wild_duck.display()

    # We can also change the quack behavior at runtime
    rubber_duck.quack_strategy = NoQuackStrategy()
    rubber_duck.display()

    # Output example:
    # wild duck can just fly and can just quack
    # cloud duck can do jet fly and can just quack
    # rubber duck can not fly and can not quack
    # wild duck can do jet fly and can just quack
    # rubber duck can not fly and can not quack
