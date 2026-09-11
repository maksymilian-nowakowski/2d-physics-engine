class Body:
    def __init__(self, position, mass, radius, restitution=0.5):
        self.position = position
        self.mass = mass
        self.radius = radius
        self.restitution = restitution

    