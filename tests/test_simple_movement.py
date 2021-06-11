from mars_rover.rover import Rover


def test_north_move_forward():
    initial_y, initial_x = 0, 0
    initial_direction = 'N'

    rover = Rover(initial_y=initial_y, initial_x=initial_x, initial_direction=initial_direction)

    rover.move(movement_direction='f')
    final_position_y, final_position_x = rover.get_position()

    assert (final_position_y, final_position_x) == (1, 0)


def test_north_move_backward():
    initial_y, initial_x = 0, 0
    initial_direction = 'N'

    rover = Rover(initial_y=initial_y, initial_x=initial_x, initial_direction=initial_direction)

    rover.move(movement_direction='b')
    final_position_y, final_position_x = rover.get_position()

    assert (final_position_y, final_position_x) == (-1, 0)


def test_east_move_forward():
    initial_y, initial_x = 0, 0
    initial_direction = 'E'

    rover = Rover(initial_y=initial_y, initial_x=initial_x, initial_direction=initial_direction)

    rover.move(movement_direction='f')
    final_position_y, final_position_x = rover.get_position()

    assert (final_position_y, final_position_x) == (0, 1)


def test_east_move_backward():
    initial_y, initial_x = 0, 0
    initial_direction = 'E'

    rover = Rover(initial_y=initial_y, initial_x=initial_x, initial_direction=initial_direction)

    rover.move(movement_direction='b')
    final_position_y, final_position_x = rover.get_position()

    assert (final_position_y, final_position_x) == (0, -1)


def test_south_move_forward():
    initial_y, initial_x = 0, 0
    initial_direction = 'S'

    rover = Rover(initial_y=initial_y, initial_x=initial_x, initial_direction=initial_direction)

    rover.move(movement_direction='f')
    final_position_y, final_position_x = rover.get_position()

    assert (final_position_y, final_position_x) == (-1, 0)


def test_south_move_backward():
    initial_y, initial_x = 0, 0
    initial_direction = 'S'

    rover = Rover(initial_y=initial_y, initial_x=initial_x, initial_direction=initial_direction)

    rover.move(movement_direction='b')
    final_position_y, final_position_x = rover.get_position()

    assert (final_position_y, final_position_x) == (1, 0)


def test_west_move_forward():
    initial_y, initial_x = 0, 0
    initial_direction = 'W'

    rover = Rover(initial_y=initial_y, initial_x=initial_x, initial_direction=initial_direction)

    rover.move(movement_direction='f')
    final_position_y, final_position_x = rover.get_position()

    assert (final_position_y, final_position_x) == (0, -1)


def test_west_move_backward():
    initial_y, initial_x = 0, 0
    initial_direction = 'W'

    rover = Rover(initial_y=initial_y, initial_x=initial_x, initial_direction=initial_direction)

    rover.move(movement_direction='b')
    final_position_y, final_position_x = rover.get_position()

    assert (final_position_y, final_position_x) == (0, 1)


def test_wrong_movement():
    initial_y, initial_x = 0, 0
    initial_direction = 'W'

    rover = Rover(initial_y=initial_y, initial_x=initial_x, initial_direction=initial_direction)

    rover.move(movement_direction='n')
