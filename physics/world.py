from physics.body import Body
from physics.vector import Vector2


class World:
    def __init__(self, gravity=Vector2(0, 9.81)):  # noqa: B008
        self.bodies = []
        self.gravity = gravity

    def add_body(self, body):
        if isinstance(body, Body) == False:
            raise ValueError("supplied object must be a Body")
        if body in self.bodies:
            raise ValueError("same body shouldn't be added twice")
        self.bodies.append(body)

    def remove_body(self, body):
        if body not in self.bodies:
            raise ValueError("body isn't currently in the world")
        self.bodies.remove(body)

    def clear(self):
        self.bodies = []

    def step(self, dt):
        for body in self.bodies:
            body.apply_force(self.gravity * body.mass)
            body.integrate(dt)
