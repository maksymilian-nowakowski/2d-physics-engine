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

def test_initial_velocity():
    body = Body(Vector2(0, 0), mass=1, radius=1)

    assert body.get_velocity(1) == Vector2(0, 0)

def test_velocity_from_position_change():
    body = Body(Vector2(0, 0), mass=1, radius=1)
    body.previous_position = Vector2(0, 0)
    body.position = Vector2(10, 5)

    assert body.get_velocity(2) == Vector2(5, 2.5)

def test_velocity_is_not_affected_by_get_velocity():
    body = Body(Vector2(0, 0), mass=1, radius=1)
    body.get_velocity(1)

    assert body.position == Vector2(0, 0)
    assert body.previous_position == Vector2(0, 0)
    assert body.acceleration == Vector2(0, 0)
    assert body.force == Vector2(0, 0)

def test_velocity_zero_dt():
    body = Body(Vector2(0, 0), mass=1, radius=1)

    with pytest.raises(ZeroDivisionError):
        body.get_velocity(0)

def test_integrate_without_force():
    body = Body(Vector2(0, 0), mass=1, radius=1)
    body.integrate(1)

    assert body.position == Vector2(0, 0)
    assert body.force == Vector2(0, 0)

def test_integrate_with_constant_force():
    body = Body(Vector2(0, 0), mass=2, radius=1)
    body.force = Vector2(10, 0)
    body.integrate(1)

    assert body.acceleration == Vector2(5, 0)
    assert body.position == Vector2(5, 0)
    assert body.previous_position == Vector2(0, 0)
    assert body.force == Vector2(0, 0)

def test_integrate_with_initial_velocity():
    body = Body(Vector2(10, 0), mass=1, radius=1)
    body.previous_position = Vector2(0, 0)
    body.integrate(1)

    assert body.position == Vector2(20, 0)
    assert body.previous_position == Vector2(10, 0)

def test_integrate_with_initial_velocity_and_force():
    body = Body(Vector2(10, 0), mass=2, radius=1)
    body.previous_position = Vector2(0, 0)
    body.force = Vector2(10, 0)
    body.integrate(1)

    assert body.position == Vector2(25, 0)