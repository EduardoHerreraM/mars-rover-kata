class MovementNotContemplatedException(Exception):
    def __init__(self, movement_direction):
        self.movement_direction = movement_direction

    def __str__(self):
        return f"'{self.movement_direction}' movement direction not contemplated"
