"""Observer pattern.

Output:
Publisher "temperature sensor 1" has data 10.0
Publisher "temperature sensor 1" has data 20.0
Publisher "temperature sensor 2" has data 30.0
Publisher "temperature sensor 2" has data 40.0
Publisher "humidity sensor 1" has data 50.0
Publisher "humidity sensor 2" has data 60.0
Publisher "humidity sensor 1" has data 70.0
Publisher "humidity sensor 2" has data 80.0
"""

from __future__ import annotations


class Group:

    def __init__(self, name: str) -> None:
        self.name = name

    def __str__(self) -> str:
        return f'"{self.name}"'

    def __repr__(self) -> str:
        return self.name


class Publisher:
    """Subject/Observable/Publisher."""

    def __init__(self, name: str) -> None:
        self.group = None
        self.name = name
        self.subscribers: dict[Group, list[Subscriber]] = {}

    def __str__(self) -> str:
        return self.name

    def __repr__(self) -> str:
        return f'"{self.name}"'

    def register(self, subscriber: Subscriber, group: Group) -> None:
        self.group = group
        self.subscribers.setdefault(group, [])
        if subscriber not in self.subscribers[group]:
            self.subscribers[group].append(subscriber)

    def deregister(self, subscriber: Subscriber, group: Group) -> None:
        if subscriber in self.subscribers[group]:
            self.subscribers[group].remove(subscriber)

    def notify(self) -> None:
        if self.group is not None:
            for subscriber in self.subscribers[self.group]:
                subscriber.update(self)


class Subscriber:
    """Observer/Subscriber/Listener."""

    def __init__(self, name: str) -> None:
        self.name = name

    def __str__(self) -> str:
        return self.name

    def __repr__(self) -> str:
        return f'"{self.name}"'

    def update(self, publisher: Publisher) -> None:
        print(f"Publisher {publisher!r} has data {publisher.data}")


class TemperatureSensor(Publisher):

    def __init__(self, name: str) -> None:
        super().__init__(name)
        self._temp = 30.0

    @property
    def data(self) -> float:
        return self._temp

    @data.setter
    def data(self, value: float) -> None:
        self._temp = float(value)
        self.notify()


class HumiditySensor(Publisher):

    def __init__(self, name: str) -> None:
        super().__init__(name)
        self._humidity = 50.0

    @property
    def data(self) -> float:
        return self._humidity

    @data.setter
    def data(self, value: float) -> None:
        self._humidity = float(value)
        self.notify()


def main() -> int:

    temperature_sensor1 = TemperatureSensor("temperature sensor 1")
    temperature_sensor2 = TemperatureSensor("temperature sensor 2")

    humidity_sensor1 = HumiditySensor("humidity sensor 1")
    humidity_sensor2 = HumiditySensor("humidity sensor 2")

    subscriber1 = Subscriber('subscriber 1')
    subscriber2 = Subscriber('subscriber 2')
    subscriber3 = Subscriber('subscriber 3')

    group1 = Group('temperature sensors')
    group2 = Group('humidity sensors')

    temperature_sensor1.register(subscriber1, group1)
    temperature_sensor2.register(subscriber2, group1)
    humidity_sensor1.register(subscriber2, group2)
    humidity_sensor2.register(subscriber3, group2)

    temperature_sensor1.data = 10
    temperature_sensor1.data = 20
    temperature_sensor2.data = 30
    temperature_sensor2.data = 40
    humidity_sensor1.data = 50
    humidity_sensor2.data = 60
    humidity_sensor1.data = 70
    humidity_sensor2.data = 80

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
