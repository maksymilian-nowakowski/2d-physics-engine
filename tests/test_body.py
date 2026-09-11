import sys
from pathlib import Path

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
