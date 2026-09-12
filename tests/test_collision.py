import pytest

from physics.body import Body
from physics.collision import check_circle_collision
from physics.vector import Vector2


def test_circles_are_not_colliding():
    body_a = Body(Vector2(0, 0), mass=1, radius=5)
    body_b = Body(Vector2(11, 0), mass=1, radius=5)

    assert check_circle_collision(body_a, body_b) == False


def test_circles_are_colliding_when_touching():
    body_a = Body(Vector2(0, 0), mass=1, radius=5)
    body_b = Body(Vector2(10, 0), mass=1, radius=5)

    assert check_circle_collision(body_a, body_b) == True


def test_overlapping_circles_are_colliding():
    body_a = Body(Vector2(0, 0), mass=1, radius=5)
    body_b = Body(Vector2(7, 0), mass=1, radius=5)

    assert check_circle_collision(body_a, body_b) == True


def test_circle_inside_another_circle_is_colliding():
    body_a = Body(Vector2(0, 0), mass=1, radius=10)
    body_b = Body(Vector2(5, 0), mass=1, radius=2)

    assert check_circle_collision(body_a, body_b) == True


def test_circles_with_different_radii():
    body_a = Body(Vector2(0, 0), mass=1, radius=3)
    body_b = Body(Vector2(7, 0), mass=1, radius=5)

    assert check_circle_collision(body_a, body_b) == True


def test_circles_are_colliding_diagonally():
    body_a = Body(Vector2(0, 0), mass=1, radius=5)
    body_b = Body(Vector2(3, 4), mass=1, radius=1)
    
    assert check_circle_collision(body_a, body_b) == True

def test_circles_at_same_position_are_colliding():
    body_a = Body(Vector2(0, 0), mass=1, radius=5)
    body_b = Body(Vector2(0, 0), mass=1, radius=5)

    assert check_circle_collision(body_a, body_b) == True

def test_body_cannot_collide_with_itself():
    body = Body(Vector2(0, 0), mass=1, radius=5)

    with pytest.raises(ValueError):
        check_circle_collision(body, body)

def test_invalid_first_body():
    body_a = Vector2(0, 0)
    body_b = Body(Vector2(10, 0), mass=1, radius=5)

    with pytest.raises(ValueError):
        check_circle_collision(body_a, body_b)

def test_invalid_second_body():
    body_a = Body(Vector2(0, 0), mass=1, radius=5)
    body_b = Vector2(10, 0)

    with pytest.raises(ValueError):
        check_circle_collision(body_a, body_b)

def test_both_bodies_invalid():
    body_a = Vector2(0, 0)
    body_b = Vector2(10, 0)

    with pytest.raises(ValueError):
        check_circle_collision(body_a, body_b)
