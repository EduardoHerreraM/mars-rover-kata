from mars_rover.exceptions import DirectionNotContemplatedError, MovementNotContemplatedException, \
    OrderNotContemplatedException, RotationNotContemplatedException
from mars_rover import settings as st


class Rover:
    def __init__(self, initial_y, initial_x, initial_direction):
        if type(initial_y) is not int or type(initial_x) is not int:
            raise TypeError
        if initial_direction not in st.VALID_DIRECTIONS:
            raise DirectionNotContemplatedError(direction=initial_direction)

        self.y = initial_y
        self.x = initial_x
        self.facing_direction = initial_direction

    def get_direction(self):
        return self.facing_direction

    def get_position(self):
        return self.y, self.x

    def move(self, movement_direction):
        if movement_direction not in st.VALID_MOVEMENT_ORDERS:
            raise MovementNotContemplatedException(movement_direction=movement_direction)
        self.x += st.MOVEMENTS[self.facing_direction][movement_direction]['x'] * st.DISTANCE_EACH_MOVEMENT
        self.y += st.MOVEMENTS[self.facing_direction][movement_direction]['y'] * st.DISTANCE_EACH_MOVEMENT

    def parse_orders(self, orders):
        for order in orders:
            if order in st.VALID_MOVEMENT_ORDERS:
                self.move(movement_direction=order)
            elif order in st.VALID_ROTATION_ORDERS:
                self.rotate(rotation_direction=order)
            else:
                raise OrderNotContemplatedException(order=order)

    def rotate(self, rotation_direction):
        if rotation_direction not in st.VALID_ROTATION_ORDERS:
            raise RotationNotContemplatedException(rotation_direction=rotation_direction)
        self.facing_direction = st.ROTATIONS[self.facing_direction][rotation_direction]
