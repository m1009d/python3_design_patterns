import abc
import logging
from typing import Union

logging.basicConfig(level=logging.INFO)


### WITHOUT PROXY
# def division(a: Union[float, int], b: Union[float, int]) ->  Union[float, int]:
#     try:
#         return a / b

#     except ZeroDivisionError:
#         logging.error('Argument b cannot be %s', {b})

#     except TypeError:
#         logging.error('Arguments must be integers or floats.')

#     return 0

# print(division(1, 2))



### WITH PROXY - doing checks after the primary class instantiation
# class Division:

#     def div(self, a: Union[float, int], b: Union[float, int]) ->  Union[float, int]:
#         return a / b


# class ProxyDivision:

#     def __init__(self):
#         self.division = Division()

#     def div(self,  a: Union[float, int], b: Union[float, int]) ->  Union[float, int]:
#         try:
#             return self.division.div(a, b)

#         except ZeroDivisionError:
#             logging.error('Argument b cannot be %s', {b})

#         except TypeError:
#             logging.error('Arguments must be integers or floats.')

#         return 0


# div = ProxyDivision()
# print(div.div(1, 0))


### WITH PROXY - doing checks before the primary class instantiation

class DivisionInterface(abc.ABC):

    @abc.abstractmethod
    def div(self, a: Union[float, int], b: Union[float, int]) ->  Union[float, int]:
        pass


class Division(DivisionInterface):

    def div(self, a: Union[float, int], b: Union[float, int]) ->  Union[float, int]:
        return a / b


class ProxyDivision(DivisionInterface):

    def __init__(self):
        self.division = Division

    def div(self,  a: Union[float, int], b: Union[float, int]) ->  Union[float, int]:
        if b == 0:
            logging.error('Argument b cannot be %s', b)
            return 0

        if not isinstance(a, (float, int)):
            logging.error('Argument "a" must be integer or float.')
            return 0

        if not isinstance(b, (float, int)):
            logging.error('Argument "b" must be integer or float.')
            return 0

        return self.division().div(a, b)


div = ProxyDivision()
print(div.div(1, 2))
