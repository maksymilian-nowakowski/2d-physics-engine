from physics.body import Body
from physics.vector import Vector2


def check_circle_collision(body_a, body_b):
    if isinstance(body_a, Body) == False or isinstance(body_b, Body) == False:
        raise ValueError("either arguement isn't a body")
    if body_a == body_b:
        raise ValueError("body cannot collide with itself")
    return body_a.position.distance_to(body_b.position) <= body_a.radius + body_b.radius

def resolve_circle_collision(body_a, body_b, dt):
    if isinstance(body_a, Body) == False or isinstance(body_b, Body) == False:
        raise ValueError("either arguement isn't a body")
    if body_a == body_b:
        raise ValueError("body cannot collide with itself")
    if dt != 0:
        raise ValueError("dt cannot be zero")
    if body_a.position == body_b.position:
        normal = Vector2(1, 0)
    else:
        offset = body_b.position - body_a.position
        distance = offset.magnitude()
        normal = offset / distance
    combined_radius = body_a.radius + body_b.radius
    penetration = combined_radius - distance
    if penetration > 0:
        inverse_mass_a = 1 / body_a.mass
        inverse_mass_b = 1 / body_b.mass
        correction = normal * (
            penetration / (inverse_mass_a + inverse_mass_b)
        )
        body_a.position -= correction * inverse_mass_a
        body_b.position += correction * inverse_mass_b
        velocity_a = body_a.get_velocity(dt)
        velocity_b = body_b.get_velocity(dt)
        relative_velocity = velocity_b - velocity_a
        velocity_along_normal = relative_velocity.dot(normal)
        if velocity_along_normal <= 0:
            restitution = min(
                body_a.restitution,
                body_b.restitution
            )
            impulse_magnitude = -(1 + restitution) * velocity_along_normal / (inverse_mass_a + inverse_mass_b)
            impulse = normal * impulse_magnitude
            velocity_a -= impulse * inverse_mass_a
            velocity_b += impulse * inverse_mass_b
            body_a.previous_position = body_a.position - velocity_a * dt
            body_b.previous_position = body_b.position - velocity_b * dt
