from mars_rover.exceptions import DirectionNotContemplatedError, MovementNotContemplatedException, \
    OrderNotContemplatedException, RotationNotContemplatedException
from mars_rover import settings as st


class Rover:
    def __init__(self, initial_y, initial_x, initial_direction):
        """
        Main constructor.

        :param initial_y: int
            Initial y axis position.
        :param initial_x: int
            Initial x axis position.
        :param initial_direction: str
            Initial facing direction.
        """

        if type(initial_y) is not int or type(initial_x) is not int or type(initial_direction) is not str:
            raise TypeError
        if initial_direction not in st.VALID_DIRECTIONS:
            raise DirectionNotContemplatedError(direction=initial_direction)

        self.y = initial_y
        self.x = initial_x
        self.facing_direction = initial_direction

    def get_direction(self):
        """
        Return current facing direction.

        :return: str
            Current facing direction.
        """

        return self.facing_direction

    def get_position(self):
        """
        Return current (y, x) position.

        :return: int, int
            Current (y, x) position.
        """

        return self.y, self.x

    def move(self, movement_direction):
        """
        Given a movement direction, if it's valid, move the rover.

        :param movement_direction: str
            Direction to move.
        """

        if movement_direction not in st.VALID_MOVEMENT_ORDERS:
            raise MovementNotContemplatedException(movement_direction=movement_direction)
        self.x += st.MOVEMENTS[self.facing_direction][movement_direction]['x'] * st.DISTANCE_EACH_MOVEMENT
        self.y += st.MOVEMENTS[self.facing_direction][movement_direction]['y'] * st.DISTANCE_EACH_MOVEMENT

    def parse_orders(self, orders):
        """
        Given a list of orders, if it's valid, perform the action.
        :param orders: list of str
            List of orders to perform.
        """

        for order in orders:
            if order in st.VALID_MOVEMENT_ORDERS:
                self.move(movement_direction=order)
            elif order in st.VALID_ROTATION_ORDERS:
                self.rotate(rotation_direction=order)
            else:
                raise OrderNotContemplatedException(order=order)

    def rotate(self, rotation_direction):
        """
        Given a rotation direction, if it's valid, rotate the rover.

        :param rotation_direction: str
            Direction to rotate to.
        """

        if rotation_direction not in st.VALID_ROTATION_ORDERS:
            raise RotationNotContemplatedException(rotation_direction=rotation_direction)
        self.facing_direction = st.ROTATIONS[self.facing_direction][rotation_direction]
