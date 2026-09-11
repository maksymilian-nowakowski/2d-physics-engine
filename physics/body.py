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
        if dt <= 0:
            raise ValueError("dt must be greater than zero")
        return (self.position - self.previous_position) / dt
