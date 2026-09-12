from physics.body import Body
from physics.vector import Vector2


def check_circle_collision(body_a, body_b):
    return body_a.position.distance_to(body_b.position) <= body_a.radius + body_b.radius
