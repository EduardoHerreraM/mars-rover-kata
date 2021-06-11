import pytest

from mars_rover import exceptions
from mars_rover.rover import Rover


def test_coordinates_not_integers_y():
    initial_y, initial_x = 'a', 0
    initial_direction = 'N'

    with pytest.raises(TypeError):
        rover = Rover(initial_y=initial_y, initial_x=initial_x, initial_direction=initial_direction)


def test_coordinates_not_integers_x():
    initial_y, initial_x = 0, 2.7
    initial_direction = 'N'

    with pytest.raises(TypeError):
        rover = Rover(initial_y=initial_y, initial_x=initial_x, initial_direction=initial_direction)


def test_direction_not_contemplated():
    initial_y, initial_x = 0, 0
    initial_direction = 'H'

    with pytest.raises(exceptions.DirectionNotContemplatedError):
        rover = Rover(initial_y=initial_y, initial_x=initial_x, initial_direction=initial_direction)
