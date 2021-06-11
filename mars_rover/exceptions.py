class DirectionNotContemplatedError(Exception):
    def __init__(self, direction):
        self.direction = direction

    def __str__(self):
        return f"'{self.direction}' direction not contemplated"


class MovementNotContemplatedException(Exception):
    def __init__(self, movement_direction):
        self.movement_direction = movement_direction

    def __str__(self):
        return f"'{self.movement_direction}' movement direction not contemplated"


class OrderNotContemplatedException(Exception):
    def __init__(self, order):
        self.order = order

    def __str__(self):
        return f"'{self.order}' order not contemplated"


class RotationNotContemplatedException(Exception):
    def __init__(self, rotation_direction):
        self.rotation_direction = rotation_direction

    def __str__(self):
        return f"'{self.rotation_direction}' rotation direction not contemplated"

