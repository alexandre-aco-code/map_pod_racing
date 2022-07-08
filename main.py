import math
import sys

# import np

# CONSTANTS
DEBUG = True
PI = math.pi

direction_compensation = 1.4  # The amount to overcompensate the direction to next checkpoint
DIST_SLOWDOWN = 2400  # At what distance from checkpoint we slow down
thrust_slowdown = 20  # What thrust when we slow down
thrust_amplitude = 140  # Amplitude of the gaussian defining the thrust
thrust_deviation = 5000  # Deviation of the gaussian defining the thrust
thrust_min = 50  # Thrust when we are going in the wrong direction
DIST_BOOST = 2500  # At what distance from checkpoint is it safe to boost
ANGLE_BOOST = 10  # At what angle from checkpoint is it safe to boost
boost = 1  # Do we have a boost
RADIUS = 600  # The radius of a checkpoint
# At what distance from checkpoint we start to turn to the next checkpoint
dist_turn = 2400
MAX_ANGLE = 120  # Clamp the target angle
MAP_CENTER = [8000, 4500]  # Center of the map


# DEBUG
def debug(*args):
    if DEBUG:
        print(*args, file=sys.stderr)


# INPUTS
def get_data():
    game_data = [int(i) for i in input().split()]
    ennemy_data = [int(i) for i in input().split()]
    return game_data + ennemy_data


# GENERAL
def flip_rotation_direction(angle, type="radians"):
    if type == "degrees":
        angle = (-angle) % 360
    elif type == "radians":
        angle = (-angle) % PI
    return angle


# CLASS
class Game:

    def __init__(self):
        pass

    def run(self):
        # x,y = pod coordonates
        # cx, cy = next checkpoint coordonnates
        # d = distance to next checkpoint
        # a = next checkpoint angle
        # ox, oy = opponents coordonates
        # t = thurst = power of ship 0 => 100
        x, y, cx, cy, d, a, ox, ox = get_data()
        t = 0
        debug(x, y, cx, cy, d, a, ox, ox)

        # debug("TESTTEST")
        # debug("TESTTEST")
        # debug("TESTTEST")

        # checkpoint est derrière
        if a > 90 or a < -90:
            t = 0

        # checkpoint est sur ls coté de ouf
        # elif a > 45 and a < 90 or a > 45 and a < -90 :
        #     t = 25

        # checkpoint est super proche
        elif d < DIST_SLOWDOWN :
            t = thrust_slowdown

        # checkpoint est tout droit super loin, on boost!
        elif a == 0 and d > 6000:
            t = "BOOST"

        # sinon vitesse max tout le temps
        else:
            t = 100

        # debug(t)

        print(cx, cy, t)


# INSTANCIATION
game = Game()

# GAME LOOP
while True:
    game.run()
