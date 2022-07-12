import math
import sys

# CONSTANTS
DEBUG = True
PI = math.pi

CHECKPOINT_RADIUS = 600  # The radius of a checkpoint
MAP_CENTER_X, MAP_CENTER_Y = [8000, 4500]  # Center of the map

DIST_SLOWDOWN = 1500  # At what distance from checkpoint we slow down
DIST_BOOST = 5000  # At what distance from checkpoint is it safe to boost

ANGLE_MAX_SPEED = 20 # angle to max thurst
ANGLE_BOOST = 2  # At what angle from checkpoint is it safe to boost

THRUST_MIN = 0  # Thrust when we are going in the wrong direction
# THRUST_SLOWDOWN = 50  # What thrust when we slow down
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

# GENERAL
def degree_to_rads(angle):
    angle = angle * (PI / 180)
    return angle

# px = py = 0
# turn = 0 

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
        # debug("turn", self.turn)

        if self.turn == 1 :
            self.px = pod_x # position au dernier tour
            self.py = pod_y
        
        vx = pod_x - self.px
        vy = pod_y - self.py

        steering_x = check_x - 2*vx
        steering_y = check_y - 2*vy

        # debug("check_x:",check_x)
        # debug("check_y:",check_y)

        # debug("steering_x:",steering_x)
        # debug("steering_y:",steering_y)

        

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




        # A fond, et on essaie de booster
        elif abs(a) <= ANGLE_MAX_SPEED :
            check_x = steering_x
            check_y = steering_y
            
            if abs(a) <= ANGLE_BOOST and d > DIST_BOOST and self.boost == 1:
                thurst = "BOOST"
                self.boost = 0
            else :
                thurst = THRUST_MAX


        # si on se rapproche du checkpoint
        # if d < DIST_SLOWDOWN and abs(a) < ANGLE_MAX_SPEED :
        #     debug("MAP CENTER")
        #     check_x = MAP_CENTER_X
        #     check_y = MAP_CENTER_Y
        #     thurst = THRUST_MIN




        # boosted = False
        # px, self.py = 0, 0      # Position im letzten Durchgang
        # turn = 0           # Nr des Durchgangs

        # while True:
        #     turn +=1

        #     .....

        #     if turn == 1:        # Zu Beginn ist die vorherige Position die aktuelle
        #         px, py = x, y

        #     steering_x, steering_y = next_checkpoint_x, next_checkpoint_y

        #     if not boosted and abs(next_checkpoint_angle) < 20 and next_checkpoint_dist > 5000:
        #         thrust = "BOOST"
        #         boosted = True

        #     elif abs(next_checkpoint_angle) > 90:
        #         thrust = 0
        #     else:
        #         thrust = 100
        #         vx = x - px          # Geschwindigkeit berechnen
        #         vy = y - py
        #         steering_x = next_checkpoint_x - 3*vx
        #         steering_y = next_checkpoint_y - 3*vy

        #     px, py, = x, y       # wir merken uns die aktuelle Position für den nächsten Durchgang

        #     print(f'{steering_x} {steering_y} {thrust}')    # mit einem f-String ist die Ausgabe bequemer






        #on ralentit proche d'un checkpoint
        # if isinstance(thurst,int):
        #     # (distanceToCheckpoint / (k*checkPointRadius)) clamped in [0,1]: we slow down as we get closer to the checkpoint.
        #     # I empirically selected the factor k=2.
        #     k = 2
        #     slowdown_at_checkpoint = 1
        #     slowdown_at_checkpoint = d / (k * CHECKPOINT_RADIUS)
        #     if slowdown_at_checkpoint > 1 :
        #         slowdown_at_checkpoint = 1
        #     elif slowdown_at_checkpoint < 0 :
        #         slowdown_at_checkpoint = 0

        #     thurst = int(thurst * slowdown_at_checkpoint)
        
        #     debug("slowdown_at_checkpoint",slowdown_at_checkpoint)




            
        # debug(pod_x, pod_y, check_x, check_y)
        debug("dist:",d)
        debug("angle:",a)
        debug("boost:", self.boost)
        debug("thurst:",thurst)

        self.px,self.py = pod_x, pod_y

        debug("check_x,check_y",check_x,check_y)

        print(check_x,check_y,thurst)


# INSTANCIATION
game = Game()

# GAME LOOP
while True:
    game.run()
