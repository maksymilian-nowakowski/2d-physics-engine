import pytest

from physics.body import Body
from physics.vector import Vector2
from physics.world import World


def test_world_initialization():
    world = World()

    assert world.bodies == []
    assert world.gravity == Vector2(0, 9.81)


def test_custom_gravity():
    world = World(Vector2(0, 5))

    assert world.gravity == Vector2(0, 5)


def test_add_body():
    world = World()
    body = Body(Vector2(0, 0), mass=1, radius=1)

    world.add_body(body)

    assert body in world.bodies
    assert len(world.bodies) == 1


def test_add_multiple_bodies():
    world = World()
    body1 = Body(Vector2(0, 0), mass=1, radius=1)
    body2 = Body(Vector2(10, 10), mass=2, radius=2)

    world.add_body(body1)
    world.add_body(body2)

    assert world.bodies == [body1, body2]


def test_body_cannot_be_added_twice():
    world = World()
    body = Body(Vector2(0, 0), mass=1, radius=1)

    world.add_body(body)

    with pytest.raises(ValueError):
        world.add_body(body)

    assert len(world.bodies) == 1


def test_invalid_body():
    world = World()

    with pytest.raises(ValueError):
        world.add_body(Vector2(0, 0))


def test_remove_body():
    world = World()
    body = Body(Vector2(0, 0), mass=1, radius=1)

    world.add_body(body)
    world.remove_body(body)

    assert body not in world.bodies
    assert world.bodies == []


def test_remove_body_that_is_not_in_world():
    world = World()
    body = Body(Vector2(0, 0), mass=1, radius=1)

    with pytest.raises(ValueError):
        world.remove_body(body)

    assert world.bodies == []


def test_clear():
    world = World()
    body1 = Body(Vector2(0, 0), mass=1, radius=1)
    body2 = Body(Vector2(10, 10), mass=2, radius=2)

    world.add_body(body1)
    world.add_body(body2)
    world.clear()

    assert world.bodies == []


def test_gravity_is_applied():
    world = World(Vector2(0, 10))
    body = Body(Vector2(0, 0), mass=2, radius=1)

    world.add_body(body)
    world.step(1)

    assert body.acceleration == Vector2(0, 10)


def test_gravity_affects_position():
    world = World(Vector2(0, 10))
    body = Body(Vector2(0, 0), mass=2, radius=1)

    world.add_body(body)
    world.step(1)

    assert body.position == Vector2(0, 10)


def test_gravity_does_not_depend_on_mass():
    world = World(Vector2(0, 10))
    body1 = Body(Vector2(0, 0), mass=1, radius=1)
    body2 = Body(Vector2(10, 0), mass=5, radius=1)

    world.add_body(body1)
    world.add_body(body2)
    world.step(1)

    assert body1.acceleration == Vector2(0, 10)
    assert body2.acceleration == Vector2(0, 10)


def test_step_updates_all_bodies():
    world = World(Vector2(0, 10))
    body1 = Body(Vector2(0, 0), mass=1, radius=1)
    body2 = Body(Vector2(10, 0), mass=1, radius=1)

    world.add_body(body1)
    world.add_body(body2)
    world.step(1)

    assert body1.position == Vector2(0, 10)
    assert body2.position == Vector2(10, 10)


def test_step_with_no_gravity():
    world = World(Vector2(0, 0))
    body = Body(Vector2(0, 0), mass=1, radius=1)

    world.add_body(body)
    world.step(1)

    assert body.position == Vector2(0, 0)


def test_world_does_not_keep_force_after_step():
    world = World(Vector2(0, 10))
    body = Body(Vector2(0, 0), mass=2, radius=1)

    world.add_body(body)
    world.step(1)

    assert body.force == Vector2(0, 0)