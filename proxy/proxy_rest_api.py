import abc
import logging
import sys
from functools import lru_cache

import requests


class GetUrlInterface(abc.ABC):

    @abc.abstractmethod
    def get_data(self, url: str) -> dict:
        pass

    @abc.abstractmethod
    def get_headers(self, data: dict) -> dict:
        pass

    @abc.abstractmethod
    def get_args(self, data: dict) -> dict:
        pass


class GetUrl(GetUrlInterface):

    def get_data(self, url: str) -> dict:
        resp = requests.get(url)
        return resp.json()

    def get_headers(self, data: dict) -> dict:
        return data['headers']

    def get_args(self, data: dict) -> dict:
        return data['args']


class GetUrlValidated(GetUrlInterface):

    def __init__(self) -> None:
        self._geturl = GetUrl()

    def get_data(self, url: str) -> dict:
        try:
            return self._geturl.get_data(url)

        except requests.ConnectTimeout:
            logging.error('Connection timeout')
            sys.exit(1)

        except requests.ReadTimeout:
            logging.error('Read timeout')
            sys.exit(1)

    def get_headers(self, data: dict) -> dict:
        logging.info('Getting headers')
        return self._geturl.get_headers(data)

    def get_args(self, data: dict) -> dict:
        logging.info('Getting args')
        return self._geturl.get_args(data)


class GetUrlCached(GetUrlInterface):

    def __init__(self) -> None:
        self._geturlvalidated = GetUrlValidated()

    @lru_cache
    def get_data(self, url: str) -> dict:
        return self._geturlvalidated.get_data(url)

    def get_headers(self, data: dict) -> dict:
        return self._geturlvalidated.get_headers(data)

    def get_args(self, data: dict) -> dict:
        return self._geturlvalidated.get_args(data)


def main() -> int:
    geturl = GetUrlCached()
    for arg in (1, 2, 3, 1, 2, 3):
        url = f'https://postman-echo.com/get?foo=bar_{arg}'
        print(f"\n {'-'*75}\n")
        data = geturl.get_data(url)
        print(data)
        print(f'Cache info: {geturl.get_data.cache_info()}')
        print(geturl.get_args(data))
        print(geturl.get_headers(data))

    return 0


if __name__ == '__main__':
    raise SystemExit(main())
