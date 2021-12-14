from dataclasses import dataclass
import typing


@dataclass
class Node:
    value: int
    left: typing.Optional['Node'] = None
    right: typing.Optional['Node'] = None
