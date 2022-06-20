"""Use proxy pattern as a simple language translator."""

from typing import Any, Union


class English:

    def __init__(self, name: str) -> None:
        self.name = name

    @property
    def hello(self) -> str:
        return f'{self.name} is saying: "Hello"'

class Slovak:

    def __init__(self, name: str) -> None:
        self.name = name

    @property
    def cau(self) -> str:
        return f'{self.name} hovori: "Cau"'

class Czech:

    def __init__(self, name: str) -> None:
        self.name = name

    @property
    def ahoj(self) -> str:
        return f'{self.name} rika: "Ahoj"'


# Proxy Pattern
# Let's just use the greet() method as s common method for all languages.
class GreetProxy:

    def __init__(self, speaker: Union[English, Slovak, Czech], speaker_method: str) -> None:
        self.speaker = speaker
        speaker_method = getattr(self.speaker, speaker_method)
        self.__setattr__('greet', speaker_method)                 # use greet() method as a translator

    # in order to get other speaker attributes, e.g. it's name.
    def __getattr__(self, attr) -> Any:
        return getattr(self.speaker, attr)


def main() -> int:
    slovak = GreetProxy(Slovak('Michal'), 'cau')
    czech = GreetProxy(Czech('Pepa'), 'ahoj')
    english = GreetProxy(English('John'), 'hello')

    print(slovak.greet)
    print(czech.greet)
    print(english.greet)
    print(f'English name is {english.name!r}')

    return 0


if __name__ == '__main__':
    raise SystemExit(main())
