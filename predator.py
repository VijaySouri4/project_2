import random

class Predator:

    def __init__(self) -> None:
        self.pos = random.choice(range(0,49))

    """Moves predator towards agent
    Returns True if moved and didn't collide with agent"""
    def move(self, environment, agent_pos):
        dist, path = environment.shortest_paths[self.pos][agent_pos]
        if dist != 0:
            self.pos = path[0]
            return True
        else:
            return False