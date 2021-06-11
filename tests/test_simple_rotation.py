from mars_rover.rover import Rover


def test_north_to_west():
    initial_y, initial_x = 0, 0
    initial_direction = 'N'

    rover = Rover(initial_y=initial_y, initial_x=initial_x, initial_direction=initial_direction)

    rover.rotate(rotation_direction='l')
    final_direction = rover.get_direction()

    assert final_direction == 'W'


def test_north_to_east():

    initial_y, initial_x = 0, 0
    initial_direction = 'N'

    rover = Rover(initial_y=initial_y, initial_x=initial_x, initial_direction=initial_direction)

    rover.rotate(rotation_direction='r')
    final_direction = rover.get_direction()

    assert final_direction == 'E'


def test_east_to_north():
    initial_y, initial_x = 0, 0
    initial_direction = 'E'

    rover = Rover(initial_y=initial_y, initial_x=initial_x, initial_direction=initial_direction)

    rover.rotate(rotation_direction='l')
    final_direction = rover.get_direction()

    assert final_direction == 'N'


def test_east_to_south():
    initial_y, initial_x = 0, 0
    initial_direction = 'E'

    rover = Rover(initial_y=initial_y, initial_x=initial_x, initial_direction=initial_direction)

    rover.rotate(rotation_direction='r')
    final_direction = rover.get_direction()

    assert final_direction == 'S'


def test_south_to_east():
    initial_y, initial_x = 0, 0
    initial_direction = 'S'

    rover = Rover(initial_y=initial_y, initial_x=initial_x, initial_direction=initial_direction)

    rover.rotate(rotation_direction='l')
    final_direction = rover.get_direction()

    assert final_direction == 'E'


def test_south_to_west():
    initial_y, initial_x = 0, 0
    initial_direction = 'S'

    rover = Rover(initial_y=initial_y, initial_x=initial_x, initial_direction=initial_direction)

    rover.rotate(rotation_direction='r')
    final_direction = rover.get_direction()

    assert final_direction == 'W'


def test_west_to_south():
    initial_y, initial_x = 0, 0
    initial_direction = 'W'

    rover = Rover(initial_y=initial_y, initial_x=initial_x, initial_direction=initial_direction)

    rover.rotate(rotation_direction='l')
    final_direction = rover.get_direction()

    assert final_direction == 'S'


def test_west_to_north():
    initial_y, initial_x = 0, 0
    initial_direction = 'W'

    rover = Rover(initial_y=initial_y, initial_x=initial_x, initial_direction=initial_direction)

    rover.rotate(rotation_direction='r')
    final_direction = rover.get_direction()

    assert final_direction == 'N'
