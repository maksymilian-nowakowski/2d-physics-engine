from vector import Vector2


class Body:
    def __init__(self, position: Vector2, mass: float, radius: float, restitution: float=0.5):
        self.position = position
        self.previous_position = position.copy()
        self.mass = mass
        self.radius = radius
        self.restitution = restitution
        self.acceleration = Vector2(0, 0)
        self.force = Vector2(0, 0)

    def apply_force(self, force):
        self.force += force

    def clear_forces(self):
        self.force = Vector2(0, 0)

    def get_velocity(self, dt):
        if dt == 0:
            raise ZeroDivisionError("dt must not be zero")
        return (self.position - self.previous_position) / dt

    def integrate(self, dt):
        """Performs one Verlet integration step."""
        self.acceleration = self.force / self.mass
        new_position = self.position + (self.position - self.previous_position) + self.acceleration * dt ** 2
        self.previous_position = self.position
        self.position = new_position
        self.clear_forces()


if __name__ == "__main__":
    # Zero force and zero initial velocity leave the body stationary.
    body = Body(Vector2(3, -2), mass=1, radius=1)
    body.integrate(0.5)
    assert body.position.x == 3 and body.position.y == -2
    assert body.previous_position.x == 3 and body.previous_position.y == -2

    # Force, mass, and timestep affect both axes correctly.
    body = Body(Vector2(0, 0), mass=2, radius=1)
    body.apply_force(Vector2(4, -6))
    body.integrate(0.5)
    assert body.position.x == 0.5 and body.position.y == -0.75
    assert body.acceleration.x == 2 and body.acceleration.y == -3

    # Forces accumulate before integration.
    body = Body(Vector2(1, 1), mass=1, radius=1)
    body.apply_force(Vector2(2, 0))
    body.apply_force(Vector2(0, 3))
    body.integrate(1)
    assert body.position.x == 3 and body.position.y == 4

    # Existing Verlet velocity is retained, and previous_position is updated.
    body = Body(Vector2(1, 2), mass=1, radius=1)
    body.previous_position = Vector2(0, 1)
    body.integrate(1)
    print(body.position)
    assert body.position.x == 2 and body.position.y == 3
    assert body.previous_position.x == 1 and body.previous_position.y == 2

    print("integrate tests passed")

