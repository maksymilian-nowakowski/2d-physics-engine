from physics.vector import Vector2
from physics.body import Body

class World:
    def __init__(self, gravity=Vector2(0, 9.81)):
        self.bodies = []
        self.gravity = gravity

    def add_body(self, body):
        if isinstance(body, Body) == False:
            raise ValueError("supplied object must be a Body")
        if body in self.bodies:
            raise ValueError("same body shouldn't be added twice")
        self.bodies.append(body)
