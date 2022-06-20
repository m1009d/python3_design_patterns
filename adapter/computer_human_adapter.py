"""Adapter python design pattern example."""

class Computer:
    """Computer is a legacy interface with execute() method."""

    def __init__(self, name) -> None:
        self.name = name

    def execute(self) -> None:
        print (f"{self.name} Computer is executing")


class Human:
    """Human is the adaptee - the new interface with new read() method."""

    def __init__(self, name) -> None:
        self.name = name

    def read(self) -> None:
        print(f"Human {self.name} is reading.")


class Adapter:
    """Client wants to use the legacy execute() method on the new Human interface."""

    def __init__(self, adaptee, adapted_method) -> None:
        self.adaptee = adaptee
        self.__dict__.update(adaptee.__dict__)

        # here is the mapping between legacy and new methods
        self.__dict__.update({'execute': adapted_method})

    def __str__(self) -> str:
        return str(self.adaptee)


def main():
    computer = Computer('Asus')
    human = Human('Michal')

    computer.execute()
    adapter = Adapter(human, human.read)
    adapter.execute()

    for obj in computer, adapter:
        print(obj.name)


if __name__ == '__main__':
    main()
