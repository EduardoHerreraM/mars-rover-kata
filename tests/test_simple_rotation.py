from mars_rover.rover import Rover


def test_north_to_east():

    initial_y, initial_x = 0, 0
    initial_direction = 'N'

    rover = Rover(initial_y=initial_y, initial_x=initial_x, initial_direction=initial_direction)

    rover.rotate('R')
    final_direction = rover.get_direction()

    assert final_direction == 'E'


def test_north_to_west():
    initial_y, initial_x = 0, 0
    initial_direction = 'N'

    rover = Rover(initial_y=initial_y, initial_x=initial_x, initial_direction=initial_direction)

    rover.rotate('L')
    final_direction = rover.get_direction()

    assert final_direction == 'W'
