import random

class Predator:

    def __init__(self) -> None:
        self.pos = random.choice(range(0,49))

    """Moves predator towards agent
    Returns True if moved and didn't collide with agent"""
    def move(self, environment, agent_pos):
        dist, paths = environment.shortest_paths[self.pos][agent_pos]
        if dist != 0: #was not properly chcecking for collision, now fixed
            options_set = set()     #creates a set for the next node options (can be created in environment)
            for i in paths:
                options_set.add(i[0])
            self.pos = random.sample(options_set, 1)[0]
            dist, path = environment.shortest_paths[self.pos][agent_pos]
            if dist == 0:
                return False
            else:
                return True
        else:
            return False