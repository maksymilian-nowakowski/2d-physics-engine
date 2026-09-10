import math

import pytest

from physics.vector import Vector2

# ─────────────────────────────────────────────
# Construction / representation
# ─────────────────────────────────────────────

def test_vector_creation():
    vector = Vector2(3, 4)

    assert vector.x == 3
    assert vector.y == 4


def test_vector_repr():
    vector = Vector2(3, 4)

    assert repr(vector) == "Vector2(3, 4)"


# ─────────────────────────────────────────────
# Arithmetic
# ─────────────────────────────────────────────

def test_vector_addition():
    a = Vector2(3, 4)
    b = Vector2(2, 1)

    result = a + b

    assert result == Vector2(5, 5)


def test_vector_subtraction():
    a = Vector2(3, 4)
    b = Vector2(2, 1)

    result = a - b

    assert result == Vector2(1, 3)


def test_vector_multiplication():
    vector = Vector2(3, 4)

    result = vector * 2

    assert result == Vector2(6, 8)


def test_vector_multiplication_by_negative_scalar():
    vector = Vector2(3, -4)

    result = vector * -2

    assert result == Vector2(-6, 8)


def test_vector_multiplication_by_zero():
    vector = Vector2(3, 4)

    result = vector * 0

    assert result == Vector2(0, 0)


def test_reverse_vector_multiplication():
    vector = Vector2(3, 4)

    result = 2 * vector

    assert result == Vector2(6, 8)


def test_vector_division():
    vector = Vector2(6, 8)

    result = vector / 2

    assert result == Vector2(3, 4)


def test_vector_division_by_zero():
    vector = Vector2(3, 4)

    with pytest.raises(ZeroDivisionError):
        vector / 0


def test_vector_negation():
    vector = Vector2(3, -4)

    result = -vector

    assert result == Vector2(-3, 4)


# ─────────────────────────────────────────────
# Magnitude
# ─────────────────────────────────────────────

def test_vector_magnitude():
    vector = Vector2(3, 4)

    assert vector.magnitude() == 5


def test_zero_vector_magnitude():
    vector = Vector2(0, 0)

    assert vector.magnitude() == 0


def test_vector_magnitude_squared():
    vector = Vector2(3, 4)

    assert vector.magnitude_squared() == 25


def test_zero_vector_magnitude_squared():
    vector = Vector2(0, 0)

    assert vector.magnitude_squared() == 0


# ─────────────────────────────────────────────
# Normalisation
# ─────────────────────────────────────────────

def test_vector_normalization():
    vector = Vector2(3, 4)

    result = vector.normalized()

    assert math.isclose(result.x, 0.6)
    assert math.isclose(result.y, 0.8)


def test_normalized_vector_has_magnitude_one():
    vector = Vector2(3, 4)

    result = vector.normalized()

    assert math.isclose(result.magnitude(), 1.0)


def test_normalizing_zero_vector():
    vector = Vector2(0, 0)

    with pytest.raises(ZeroDivisionError):
        vector.normalized()


# ─────────────────────────────────────────────
# Dot product
# ─────────────────────────────────────────────

def test_dot_product():
    a = Vector2(3, 4)
    b = Vector2(2, 1)

    assert a.dot(b) == 10


def test_dot_product_perpendicular_vectors():
    a = Vector2(1, 0)
    b = Vector2(0, 1)

    assert a.dot(b) == 0


def test_dot_product_with_zero_vector():
    a = Vector2(3, 4)
    b = Vector2(0, 0)

    assert a.dot(b) == 0


# ─────────────────────────────────────────────
# Distance
# ─────────────────────────────────────────────

def test_distance_between_vectors():
    a = Vector2(0, 0)
    b = Vector2(3, 4)

    assert a.distance_to(b) == 5


def test_distance_to_same_position():
    a = Vector2(3, 4)

    assert a.distance_to(a) == 0


# ─────────────────────────────────────────────
# Copy
# ─────────────────────────────────────────────

def test_vector_copy():
    original = Vector2(3, 4)
    copy = original.copy()

    assert copy == original
    assert copy is not original


def test_modifying_copy_does_not_modify_original():
    original = Vector2(3, 4)
    copy = original.copy()

    copy.x = 10

    assert original.x == 3
    assert copy.x == 10


# ─────────────────────────────────────────────
# Equality
# ─────────────────────────────────────────────

def test_equal_vectors():
    a = Vector2(3, 4)
    b = Vector2(3, 4)

    assert a == b


def test_unequal_vectors():
    a = Vector2(3, 4)
    b = Vector2(4, 3)

    assert a != b


def test_vectors_with_different_x_values_are_not_equal():
    a = Vector2(3, 4)
    b = Vector2(5, 4)

    assert a != b


def test_vectors_with_different_y_values_are_not_equal():
    a = Vector2(3, 4)
    b = Vector2(3, 5)

    assert a != b