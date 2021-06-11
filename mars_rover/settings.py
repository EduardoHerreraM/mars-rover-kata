DISTANCE_EACH_MOVEMENT = 1

MOVEMENTS = {
    'N': {
        'f': {
            'x': 0,
            'y': 1
        },
        'b': {
            'x': 0,
            'y': -1
        }
    },
    'E': {
        'f': {
            'x': 1,
            'y': 0
        },
        'b': {
            'x': -1,
            'y': 0
        }
    },
    'S': {
        'f': {
            'x': 0,
            'y': -1
        },
        'b': {
            'x': 0,
            'y': 1
        }
    },
    'W': {
        'f': {
            'x': -1,
            'y': 0
        },
        'b': {
            'x': 1,
            'y': 0
        }
    }
}

ROTATIONS = {
    'N': {
        'l': 'W',
        'r': 'E'
    },
    'E': {
        'l': 'N',
        'r': 'S'
    },
    'S': {
        'l': 'E',
        'r': 'W'
    },
    'W': {
        'l': 'S',
        'r': 'N'
    }
}

VALID_MOVEMENT_ORDERS = ['f', 'b']
VALID_ROTATION_ORDERS = ['l', 'r']
