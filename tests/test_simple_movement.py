from mars_rover.rover import Rover


def test_move_up():
    initial_y, initial_x = 0, 0
    initial_direction = 'N'

    rover = Rover(initial_y=initial_y, initial_x=initial_x, initial_direction=initial_direction)

    rover.move(direction='f')
    final_position_y, final_position_x = rover.get_position()

    assert (final_position_y, final_position_x) == (1, 0)
