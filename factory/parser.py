#!/usr/bin/env python3

"""Factory pattern.

In this case we are using function as a factory.
"""

import json
from abc import ABC, abstractmethod
from xml.etree import ElementTree


class Parser(ABC):

    @abstractmethod
    def parse(self) -> dict:
        ...


class JSONParser(Parser):

    def __init__(self, filepath: str) -> None:
        with open(filepath, encoding='utf-8', mode='r') as fh:
            self.data = json.load(fh)

    @property
    def parse(self) -> dict:
        return self.data


class XMLParser(Parser):

    def __init__(self, filepath: str) -> None:
        self.data = ElementTree.parse(filepath)

    @property
    def parse(self):
        return self.data


def parser_factory(filepath: str) -> Parser:
    """Factory function."""

    if filepath.endswith('json'):
        parser = JSONParser
    elif filepath.endswith('xml'):
        parser = XMLParser
    else:
        raise ValueError(f'Cannot connect to {filepath}')

    return parser(filepath)


def main() -> int:
    json_data = parser_factory('my_file.json')
    # do som magic with json_data

    xml_data = parser_factory('my_file.xml')
    # do som magic with xml_data

    return 0


if __name__ == "__main__":

    raise SystemExit(main())
