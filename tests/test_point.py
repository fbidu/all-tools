"""
Unit tests for a 3D point class
"""
import hypothesis
import hypothesis.strategies as st

from all_tools.point import Point


# pylint:disable=invalid-name
def test_attributes():
    """
    Can we set a point's attributes?
    """
    point = Point(1, 2, 3)
    assert (point.x, point.y, point.z) == (1, 2, 3)
    point.x = 4
    assert point.x == 4


def test_string_representation():
    """
    Does a point have meaningful repr and str?
    """
    point = Point(1, 2, 3)
    assert str(point) == "Point(x=1, y=2, z=3)"
    assert repr(point) == "Point(x=1, y=2, z=3)"
    point.y = 4
    assert str(point) == "Point(x=1, y=4, z=3)"
    assert repr(point) == "Point(x=1, y=4, z=3)"


def test_equality_and_inequality():
    """
    Does equality work?
    """
    p1 = Point(1, 2, 3)
    p2 = Point(1, 2, 4)
    p3 = Point(1, 2, 3)
    assert Point(1, 2, 3) != Point(1, 2, 4)
    assert Point(1, 2, 3) == Point(1, 2, 3)

    assert p1 != p2
    assert p1 == p3
    p3.x, p3.z = p3.z, p3.x
    assert p1 != p3
    assert p1 != p3


def test_shifting():
    """
    Can we add and subtract points from one another?
    """
    p1 = Point(1, 2, 3)
    p2 = Point(4, 5, 6)
    p3 = p2 + p1
    p4 = p3 - p1
    assert (p3.x, p3.y, p3.z) == (5, 7, 9)
    assert (p4.x, p4.y, p4.z) == (p2.x, p2.y, p2.z)


def test_scale():
    """
    Can we multiply a point by a scalar?
    """
    p1 = Point(1, 2, 3)
    p2 = p1 * 2
    assert (p2.x, p2.y, p2.z) == (2, 4, 6)
    p3 = 3 * p1
    assert (p3.x, p3.y, p3.z) == (3, 6, 9)


def test_iterable_point():
    """
    Can we iterate over a point?
    """
    point = Point(x=1, y=2, z=3)
    x, y, z = point
    assert (x, y, z) == (1, 2, 3)


@hypothesis.settings(verbosity=hypothesis.Verbosity.verbose)
@hypothesis.given(st.tuples(st.floats(), st.floats(), st.floats()))
def test_properties_init(p):
    """
    Can we initialize a bunch of points?
    """
    point = Point(*p)
    assert point


@hypothesis.given(
    st.builds(
        Point,
        st.floats(allow_nan=False, allow_infinity=False),
        st.floats(allow_nan=False, allow_infinity=False),
        st.floats(allow_nan=False, allow_infinity=False),
    ),
    st.builds(
        Point,
        st.floats(allow_nan=False, allow_infinity=False),
        st.floats(allow_nan=False, allow_infinity=False),
        st.floats(allow_nan=False, allow_infinity=False),
    ),
)
def test_commutative_sum(p_1, p_2):
    """
    Is the sum of point commutative?
    """
    assert p_1 + p_2 == p_2 + p_1


@hypothesis.given(
    st.builds(
        Point,
        st.floats(allow_nan=False, allow_infinity=False),
        st.floats(allow_nan=False, allow_infinity=False),
        st.floats(allow_nan=False, allow_infinity=False),
    ),
    st.floats(allow_nan=False, allow_infinity=False),
)
def test_scaling(p, x):
    """
    Can we multiply a point by a scalar?
    """
    p_2 = p * x
    assert (p_2.x, p_2.y, p_2.z) == (p.x * x, p.y * x, p.z * x)
