from mars_rover import settings as st


class Rover:
    def __init__(self, initial_y, initial_x, initial_direction):
        self.y = initial_y
        self.x = initial_x
        self.direction = initial_direction

    def get_direction(self):
        return self.direction

    def get_position(self):
        return self.y, self.x

    def move(self, direction):
        self.x += st.MOVEMENTS[self.direction][direction]['x'] * st.DISTANCE_EACH_MOVEMENT
        self.y += st.MOVEMENTS[self.direction][direction]['y'] * st.DISTANCE_EACH_MOVEMENT

    def rotate(self, rotation_direction):
        self.direction = st.ROTATIONS[self.direction][rotation_direction]
