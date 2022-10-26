import random

class Predator:

    def __init__(self) -> None:
        self.pos = random.choice(range(0,49))

    """Moves predator towards agent
    Returns True if moved and didn't collide with agent"""
    def move(self, environment, agent_pos):
        dist, path = environment.shortest_paths[self.pos][agent_pos]
        if dist != 0: #was not properly chcecking for collision, now fixed
            self.pos = random.choice(path)[0]
            dist, path = environment.shortest_paths[self.pos][agent_pos]
            if dist == 0:
                return False
            else:
                return True
        else:
            return False