from physics.vector import Vector2


class World:
    def __init__(self, gravity=Vector2(0, 9.81)):
        self.bodies = []
        self.gravity = gravity
