from physics.vector import Vector2


class Body:
    def __init__(self, position: Vector2, mass: float, radius: float, restitution: float=0.5):
        self.position = position
        self.previous_position = position.copy()
        self.mass = mass
        self.radius = radius
        self.restitution = restitution
        self.acceleration = Vector2(0, 0)
        self.force = Vector2(0, 0)

