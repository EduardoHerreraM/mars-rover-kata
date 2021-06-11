from mars_rover import settings as st


class Rover:
    def __init__(self, initial_y, initial_x, initial_direction):
        self.y = initial_y
        self.x = initial_x
        self.facing_direction = initial_direction

    def get_direction(self):
        return self.facing_direction

    def get_position(self):
        return self.y, self.x

    def move(self, movement_direction):
        self.x += st.MOVEMENTS[self.facing_direction][movement_direction]['x'] * st.DISTANCE_EACH_MOVEMENT
        self.y += st.MOVEMENTS[self.facing_direction][movement_direction]['y'] * st.DISTANCE_EACH_MOVEMENT

    def rotate(self, rotation_direction):
        self.facing_direction = st.ROTATIONS[self.facing_direction][rotation_direction]
