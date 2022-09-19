import re
from typing import Iterator, List, Iterable, Union


class Search:

    def filter(self: Iterator, string_to_search: str) -> Iterable:
        if not isinstance(string_to_search, str):
            raise TypeError("В функцию фильтра переданы неверные данные, разрешены только строки")
        return list(filter(lambda line: string_to_search in line, self))

    def sort(self: Iterator, order: str = 'asc') -> List:
        if order not in ('asc', 'desc'):
            raise ValueError('В функцию сортировки передан неверный аргумент, разрешено использовать '
                             'только по возрастанию или по убыванию')
        if order == 'desc':
            return sorted(self, reverse=True)
        return list(sorted(self, reverse=False))

    def map(self: Iterator, column: Union[str, int]) -> Iterable:
        regex = re.compile(r'(?: - - \[)|(?:\] ")|(?:" ")|(?: \")|(?:\" )')
        if not str(column).isdigit():
            raise TypeError('Нужно передавать цифру в качестве номера столбца в функцию карты')
        return map(lambda line: regex.split(line)[int(column)], self)

    def limit(self: Iterator, number: Union[str, int]) -> List:
        if not str(number).isdigit():
            raise TypeError('Разрешены только цифры')
        return list(self)[:int(number)]

    def unique(self: Iterator) -> Iterable:
        return set(self)

    def regex(self: Iterator, expression: str) -> Iterable:
        regex = re.compile(rf'{str(expression)}')
        return filter(lambda line: regex.search(line), self)