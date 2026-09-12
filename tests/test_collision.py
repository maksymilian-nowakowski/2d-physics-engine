import pytest

from physics.body import Body
from physics.collision import check_circle_collision
from physics.vector import Vector2


def test_circles_are_not_colliding():
    body_a = Body(Vector2(0, 0), mass=1, radius=5)
    body_b = Body(Vector2(11, 0), mass=1, radius=5)

    assert check_circle_collision(body_a, body_b) == False
