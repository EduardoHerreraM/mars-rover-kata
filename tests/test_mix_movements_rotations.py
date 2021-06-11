import pytest

from mars_rover import exceptions
from mars_rover.rover import Rover


def test_mix_1():
    initial_y, initial_x = 0, 0
    initial_direction = 'N'

    rover = Rover(initial_y=initial_y, initial_x=initial_x, initial_direction=initial_direction)

    orders = ['f', 'f', 'l']

    rover.parse_orders(orders=orders)

    final_position_y, final_position_x = rover.get_position()
    final_direction = rover.get_direction()

    assert (final_position_y, final_position_x) == (2, 0) and final_direction == 'W'


def test_mix_2():
    initial_y, initial_x = 0, 0
    initial_direction = 'N'

    rover = Rover(initial_y=initial_y, initial_x=initial_x, initial_direction=initial_direction)

    orders = ['r', 'f', 'f', 'l', 'f', 'l', 'b', 'r', 'f', 'f', 'l', 'f', 'r', 'b', 'r', 'b', 'l', 'f', 'f', 'l', 'l']

    rover.parse_orders(orders=orders)

    final_position_y, final_position_x = rover.get_position()
    final_direction = rover.get_direction()

    assert (final_position_y, final_position_x) == (4, 1) and final_direction == 'S'


def test_wrong_order():
    initial_y, initial_x = 0, 0
    initial_direction = 'N'

    rover = Rover(initial_y=initial_y, initial_x=initial_x, initial_direction=initial_direction)

    orders = ['f', 'f', 'f', 'f', 'f', 'p']

    with pytest.raises(expected_exception=exceptions.OrderNotContemplatedException):
        rover.parse_orders(orders=orders)
