import pytest

from physics.body import Body
from physics.vector import Vector2


def test_body_initialization():
    body = Body(Vector2(10, 20), mass=5, radius=3, restitution=0.7)

    assert body.position == Vector2(10, 20)
    assert body.previous_position == Vector2(10, 20)
    assert body.mass == 5
    assert body.radius == 3
    assert body.restitution == 0.7
    assert body.acceleration == Vector2(0, 0)
    assert body.force == Vector2(0, 0)