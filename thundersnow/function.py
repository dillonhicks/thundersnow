# -*- coding: utf-8 -*-
import functools
from typing import Sized, TypeVar, Union, Optional, Iterable, Sequence


__all__ = (
    'maybe',
    'maybe_str',
    'maybe_bool',
    'maybe_int',
    'first',
    'last',
)


T = TypeVar('T')
S = TypeVar('S')


class maybe(object):
    """
     Shorthand for the ugly python ternary::

        val = obj if obj is not None else other

    """

    def __init__(self, value):
        # type: (Optional[T]) -> None
        self._value = value

    def else_(self, other):
        # type: (S) -> Union[T, S]
        if self._value is None:
            return other
        return self._value


class given(maybe):
    """
    given(obj).may_have('hello').else_(str)
    """
    def may_have(self, name):
        # type: (str) -> maybe
        return maybe(getattr(self._value, name, None))


def first(iterable, or_=None):
    """

    For simple case of a list this is about 3x slower than::

        val = x[0] if len(x) > 0 else or_

    """
    # type: (Iterable[T], T) -> Optional[T]
    return next(iter(iterable), or_)


def last(iterable, or_=None):
    # type: (Sized[T], T) -> Optional[T]
    """Force iterable to be a Sequence on :func:`last` so last cannot be
    called on infinite iterators and generators.

    In the simple list/str case this is about 10x slower than x[-1].
    """
    try:
        return next(iter(reversed(iterable)))
    except StopIteration:
        return or_
