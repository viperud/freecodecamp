import copy
import random

class Hat:
    contents = []
    def __init__(self, **args):
        self.contents = [k for k, v in args.items() for _ in range(v)]

    def draw(self, balls):
        draws = min(balls, len(self.contents))
        draw_ball = []
        for _ in range(draws):
            draw_ball.append(self.contents.pop(random.randrange(len(self.contents))))

        return draw_ball

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    M = 0
    for i in range(num_experiments):
        hat2 = copy.deepcopy(hat)
        result = hat2.draw(num_balls_drawn)
        balls_req = sum([1 for k, v in expected_balls.items() if result.count(k) >= v])
        M += 1 if balls_req == len(expected_balls) else 0

    return M / num_experiments

hat1 = Hat(yellow=3, blue=2, green=6)
hat2 = Hat(red=5, orange=4)
hat3 = Hat(red=5, orange=4, black=1, blue=0, pink=2, striped=9)

hat = Hat(black=6, red=4, green=3)
probability = experiment(hat=hat, expected_balls={'red':2,'green':1}, num_balls_drawn=5, num_experiments=2000)
print(probability)