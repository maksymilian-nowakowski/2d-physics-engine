import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "physics"))

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


def test_previous_position_is_independent():
    body = Body(Vector2(0, 0), mass=1, radius=1)
    body.position = Vector2(10, 20)

    assert body.previous_position == Vector2(0, 0)


def test_invalid_mass():
    for invalid_mass in (0, -1):
        with pytest.raises(ValueError):
            Body(Vector2(0, 0), mass=invalid_mass, radius=1)


def test_invalid_radius():
    for invalid_radius in (0, -1):
        with pytest.raises(ValueError):
            Body(Vector2(0, 0), mass=1, radius=invalid_radius)


def test_invalid_restitution():
    for invalid_restitution in (-0.1, 1.1):
        with pytest.raises(ValueError):
            Body(Vector2(0, 0), mass=1, radius=1, restitution=invalid_restitution)

    for valid_restitution in (0, 1):
        body = Body(Vector2(0, 0), mass=1, radius=1, restitution=valid_restitution)
        assert body.restitution == valid_restitution

def test_apply_force():
    body = Body(Vector2(0, 0), mass=1, radius=1)
    body.apply_force(Vector2(10, 5))

    assert body.force == Vector2(10, 5)

def test_multiple_forces_accumulate():
    body = Body(Vector2(0, 0), mass=1, radius=1)
    body.apply_force(Vector2(10, 5))
    body.apply_force(Vector2(-3, 2))

    assert body.force == Vector2(7, 7)

def test_clear_forces():
    body = Body(Vector2(0, 0), mass=1, radius=1)
    body.apply_force(Vector2(10, 5))
    body.clear_forces()

    assert body.force == Vector2(0, 0)