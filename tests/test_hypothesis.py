"""
A lot of different tests with hypothesis
"""
import math as m

import hypothesis.strategies as st
import hypothesis as ht
import pytest

# pylint:disable=missing-function-docstring
@pytest.mark.xfail
@ht.settings(verbosity=ht.Verbosity.verbose)
@ht.given(st.integers(), st.integers())
def test_floats_are_commutative(x, y):
    assert x + y == y + x


@pytest.mark.xfail
@ht.given(st.floats(min_value=0))
def test_squared_roots_squared(x):
    assert m.sqrt(x) ** 2 == x
