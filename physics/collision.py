from physics.body import Body
from physics.vector import Vector2


def check_circle_collision(body_a, body_b):
    if isinstance(body_a, Body) == False or isinstance(body_b, Body) == False:
        raise ValueError("either arguement isn't a body")
    if body_a == body_b:
        raise ValueError("body cannot collide with itself")
    return body_a.position.distance_to(body_b.position) <= body_a.radius + body_b.radius
