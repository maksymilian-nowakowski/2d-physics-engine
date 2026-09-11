from vector import Vector2


class Body:
    def __init__(self, position: Vector2, mass: float, radius: float, restitution: float=0.5):
        self.position = position
        self.previous_position = position.copy()
        if mass <= 0:
            raise ValueError("mass cannot be equal to or less than zero")
        self.mass = mass
        if radius <= 0:
            raise ValueError("radius cannot be equal to or less than zero")
        self.radius = radius
        if restitution < 0 or restitution > 1:
            raise ValueError("restituion must be between zero and one")
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

body = Body(Vector2(0, 0), 2, 5)

body.apply_force(Vector2(10, 0))

body.integrate(1)

print(body.position)
print(body.previous_position)
print(body.acceleration)
print(body.force)

print(body.get_velocity(1))