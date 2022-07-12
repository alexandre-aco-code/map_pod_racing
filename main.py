import math
import sys

# CONSTANTS
DEBUG = True
CHECKPOINT_RADIUS = 600  # The radius of a checkpoint
DIST_SLOWDOWN = 1500  # At what distance from checkpoint we slow down
DIST_BOOST = 5000  # At what distance from checkpoint is it safe to boost
ANGLE_MAX_SPEED = 20 # angle to max thurst
ANGLE_BOOST = 2  # At what angle from checkpoint is it safe to boost
THRUST_MIN = 0  # Thrust when we are going in the wrong direction
THRUST_MAX = 100

# DEBUG
def debug(*args):
    if DEBUG:
        print(*args, file=sys.stderr)

# INPUTS
def get_data():
    game_data = [int(i) for i in input().split()]
    ennemy_data = [int(i) for i in input().split()]
    return game_data + ennemy_data

# CLASS
class Game:

    boost = 1
    turn = 0
    px = py = 0
    
    def __init__(self):
        pass

    def run(self):
        # x,y = pod coordonates
        # check_x, check_y = next checkpoint coordonnates
        # d = distance to next checkpoint
        # a = next checkpoint angle
        # ox, oy = opponents coordonates
        # t = thurst = power of ship 0 => 100
        pod_x, pod_y, check_x, check_y, d, a, ox, ox = get_data()
        thurst = 100

        self.turn = self.turn + 1

        if self.turn == 1 :# au premier tour, position au dernier tour = position actuelle
            self.px = pod_x 
            self.py = pod_y
        
        vx = pod_x - self.px
        vy = pod_y - self.py

        steering_x = check_x - 2*vx
        steering_y = check_y - 2*vy

        # checkpoint est derrière
        if abs(a) > 90:
            thurst = THRUST_MIN

        # checkpoint est un peu sur le coté
        elif ANGLE_MAX_SPEED <= abs(a) <= 90 :

            # (1 - angle/90) clamped in [0,1]: the more misaligned we are, the more we slow down.
            slowdown_for_rotation = 1 - abs(a/90)
        
            # debug("slowdown_for_rotation",slowdown_for_rotation)
            thurst = int(THRUST_MAX * slowdown_for_rotation)

            check_x = steering_x
            check_y = steering_y

        # Checkpoint est devant => A fond! Et on essaie de booster
        elif abs(a) <= ANGLE_MAX_SPEED :
            check_x = steering_x
            check_y = steering_y
            
            if abs(a) <= ANGLE_BOOST and d > DIST_BOOST and self.boost == 1:
                thurst = "BOOST"
                self.boost = 0
            else :
                thurst = THRUST_MAX

        debug("dist:",d)
        debug("angle:",a)
        debug("boost:", self.boost)
        debug("thurst:",thurst)

        #on save les coordonnées du pod dans px py pour le tour d'après
        self.px,self.py = pod_x, pod_y

        print(check_x,check_y,thurst)


# INSTANCIATION
game = Game()

# GAME LOOP
while True:
    game.run()
