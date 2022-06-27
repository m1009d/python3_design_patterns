"""Observer pattern.

Output:
subscriber 1 notification received: hello from publisher 1, group: group 1
subscriber 2 notification received: hello from publisher 1, group: group 1
subscriber 3 notification received: hello from publisher 1, group: group 1
subscriber 1 notification received: hello from publisher 1, group: group 2
"""


from typing import Dict, List


class Group:

    def __init__(self, name: str) -> None:
        self.name = name

    def __str__(self) -> str:
        return self.name


class Publisher:
    """Subject/Observable/Publisher."""

    def __init__(self, name: str) -> None:
        self.name = name
        self.subscribers: Dict[Group, List['Subscriber']] = {}

    def __str__(self) -> str:
        return self.name

    def register(self, subscriber: 'Subscriber', group: Group) -> None:
        self.subscribers.setdefault(group, [])
        if subscriber not in self.subscribers[group]:
            self.subscribers[group].append(subscriber)

    def deregister(self, subscriber: 'Subscriber', group: Group) -> None:
        if subscriber in self.subscribers[group]:
            self.subscribers[group].remove(subscriber)

    def notify(self, group: Group) -> None:
        for subscriber in self.subscribers[group]:
            subscriber.read(f'hello from {self}, group: {group}')


class Subscriber:
    """Observer/Subscriber/Listener."""

    def __init__(self, name: str) -> None:
        self.name = name

    def __str__(self) -> str:
        return self.name

    def read(self, msg: str) -> None:
        print(f'{self} notification received: {msg}')




def main() -> int:

    subscriber1 = Subscriber('subscriber 1')
    subscriber2 = Subscriber('subscriber 2')
    subscriber3 = Subscriber('subscriber 3')

    group1 = Group('group 1')
    group2 = Group('group 2')

    publisher = Publisher('publisher 1')

    publisher.register(subscriber1, group1)
    publisher.register(subscriber2, group1)
    publisher.register(subscriber3, group1)
    publisher.register(subscriber1, group2)

    publisher.notify(group1)
    publisher.notify(group2)

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
