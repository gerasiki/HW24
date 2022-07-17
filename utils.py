from typing import Iterator, Union, List, Generator
import re


def get_by_limit(file: List, limit: int) -> Generator:
    yield file[:limit]


def build_query(cmd: str, val: Union[str, int], file: Iterator) -> Iterator:
    if cmd == 'filter':
        return iter(filter(lambda x: val in x, file))
    if cmd == 'map':
        i = int(val)
        return iter(map(lambda v: v.split(' ')[i], file))
    if cmd == 'unique':
        return iter(set(file))
    if cmd == "sort":
        reverse = val == 'desc'
        return iter(sorted(file, reverse=reverse))
    if cmd == 'limit':
        i = int(val)
        return iter(get_by_limit(list(file), i))
    if cmd == 'regex':
        regex = re.compile(str(val))
        return iter(filter(lambda x: regex.search(x), file))
    return iter(file)
