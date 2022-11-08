import random

class Prey:

    def __init__(self) -> None:
        self.pos = random.choice(range(0,49))

    """Moves prey with 1/degree + 1 probability of staying still or moving to three other nodes
    Returns True if moved and didn't collide with agent"""
    def move(self, environment, agent_pos):
        if environment.lis[self.pos].degree == 2:
            options = [environment.lis[self.pos].index, environment.lis[self.pos].left_node_index,  environment.lis[self.pos].right_node_index]
        else:
            options = [environment.lis[self.pos].index, environment.lis[self.pos].left_node_index,  environment.lis[self.pos].right_node_index,  environment.lis[self.pos].other_node_index]
        self.pos = random.choice(options)
        if agent_pos == self.pos:
            return False
        else:
            return True