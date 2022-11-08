import random
import predator
import prey
import environment
import numpy as np

class Agent_2:

    def __init__(self, input_predator = None, input_prey = None, input_environment = None, input_pos = None) -> None:
        if input_predator is None:
            self.predator = predator.Predator()
        else: 
            self.predator = input_predator
        
        if input_prey is None:
            self.prey = prey.Prey()
        else:
            self.prey = input_prey

        if input_environment is None:
            self.environment = environment.Env(50)
        else:
            self.environment = input_environment
        
        if input_pos is None:
            self.pos = random.choice(range(0,49))
        else:
            self.pos = input_pos

        self.steps = 0

        #make sure agent doesnt start in occupied node
        while self.prey.pos == self.pos or self.predator.pos == self.pos:
            self.pos = random.choice(range(0,49))

    """Movement function for agent 1
    returns 1 if catches prey, 0 if dies, -1 if timeout"""

    def move(self):
        #runs for 100 steps else returns false
        while self.steps < 100:
            actual_predator_pos = self.predator.pos
            actual_prey_pos = self.prey.pos
            current_node = self.environment.lis[self.pos]
            shortest_paths = self.environment.shortest_paths
            
            adjacent_nodes = [current_node.left_node_index,
            current_node.right_node_index,
            current_node.other_node_index, self.pos]

            #Bellmans Eq for each of the possible routines (actions agent can take)

            if current_node.degree == 3:
                routine_left_predator_utility = (0.9 ** shortest_paths[current_node.left_node_index][actual_predator_pos])
                routine_right_predator_utility = (0.9 ** shortest_paths[current_node.right_node_index][actual_predator_pos])
                routine_cur_predator_utility = (0.9 ** shortest_paths[current_node.index][actual_predator_pos])
                routine_other_predator_utility = (0.9 ** shortest_paths[current_node.other_node_index][actual_predator_pos])
                predator_choices = np.array([routine_left_predator_utility, routine_right_predator_utility, routine_other_predator_utility, routine_cur_predator_utility])
            else:
                routine_left_predator_utility = (0.9 ** shortest_paths[current_node.left_node_index][actual_predator_pos])
                routine_right_predator_utility = (0.9 ** shortest_paths[current_node.right_node_index][actual_predator_pos])
                routine_cur_predator_utility = (0.9 ** shortest_paths[current_node.index][actual_predator_pos])
                predator_choices = np.array([routine_left_predator_utility, routine_right_predator_utility, np.Infinity, routine_cur_predator_utility])

            if current_node.degree == 3:
                routine_left_prey_utility = (0.9 ** shortest_paths[current_node.left_node_index][actual_prey_pos])
                routine_right_prey_utility = (0.9 ** shortest_paths[current_node.right_node_index][actual_prey_pos])
                routine_cur_prey_utility = (0.9 ** shortest_paths[current_node.index][actual_prey_pos])
                routine_other_prey_utility = (0.9 ** shortest_paths[current_node.other_node_index][actual_prey_pos])
                prey_choices = np.array([routine_left_prey_utility, routine_right_prey_utility, routine_other_prey_utility, routine_cur_prey_utility])
            else:
                routine_left_prey_utility = (0.9 ** shortest_paths[current_node.left_node_index][actual_prey_pos])
                routine_right_prey_utility = (0.9 ** shortest_paths[current_node.right_node_index][actual_prey_pos])
                routine_cur_prey_utility = (0.9 ** shortest_paths[current_node.index][actual_prey_pos])
                prey_choices = np.array([routine_left_prey_utility, routine_right_prey_utility, 0, routine_cur_prey_utility])
            
            choices = prey_choices - predator_choices

            results =  np.where(np.isclose(choices, np.amax(choices)))[0]
            self.pos = adjacent_nodes[np.random.choice(results)]
            self.steps += 1

            #returns 0 if moves into predator or predator moves into it
            if actual_predator_pos == self.pos: 
                return 0, self.steps
            #returns 1 if moves into prey 
            if actual_prey_pos == self.pos:
                return 1, self.steps
            #returns 1 if prey moves into it
            if not self.prey.move(self.environment,self.pos):
                return 1, self.steps
            #returns 0 if predator moves into it
            if not self.predator.move(self.environment,self.pos):
                return 0, self.steps
        #returns -1 if timeout
        return -1, self.steps
