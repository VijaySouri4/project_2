import random
import predator
import prey
import environment

class Agent_1:

    def __init__(self, predator = predator.Predator(), prey = prey.Prey(), environment = environment.Env(50), pos = random.choice(range(0,49))) -> None:
        self.predator = predator
        self.prey = prey
        self.environment = environment
        self.steps = 0
        self.pos = pos
        #make sure agent doesnt start in occupied node
        while self.prey.pos == self.pos or self.prey.pos == self.pos:
            self.pos = random.choice(range(0,49))

    """Movement function for agent 1
    returns 1 if catches prey, 0 if dies, -1 if timeout"""

    def move(self):
        #runs for 100 steps else returns false
        while self.steps < 100:
            self.steps += 1
            predator_pos = self.predator.pos
            prey_pos = self.prey.pos
            current_node = self.environment.lis[self.pos]
            shortest_paths = self.environment.shortest_paths

            #array of possible choices
            adjacent_nodes = [current_node.left_node_index,
            current_node.left_node_index,
            current_node.other_node_index]

            #gets distances to predator from each direction
            left_pred_dist = shortest_paths[current_node.left_node_index][predator_pos][0]
            right_pred_dist = shortest_paths[current_node.right_node_index][predator_pos][0]
            other_pred_dist = shortest_paths[current_node.other_node_index][predator_pos][0]
            cur_pred_dist = shortest_paths[self.pos][predator_pos][0]

            #puts distances from predator in array
            pred_dist_array = [left_pred_dist, right_pred_dist, other_pred_dist]

            #gets distances to prey from each direction
            left_prey_dist = shortest_paths[current_node.left_node_index][prey_pos][0]
            right_prey_dist = shortest_paths[current_node.right_node_index][prey_pos][0]
            other_prey_dist = shortest_paths[current_node.other_node_index][prey_pos][0]
            cur_prey_dist = shortest_paths[self.pos][prey_pos][0]

            #puts distances from prey in array
            prey_dist_array = [left_prey_dist, right_prey_dist, other_prey_dist]

            #creates array of length 7, each index corresponding to the possible scenarios outlined in writeup
            #please check if this what the writeup meant
            options = [[] for i in range(7)]
            for i in range(len(prey_dist_array)):
                if prey_dist_array[i] < cur_prey_dist and pred_dist_array[i] > cur_pred_dist:
                    options[0].append(adjacent_nodes[i])
                elif prey_dist_array[i] < cur_prey_dist:
                    options[1].append(adjacent_nodes[i])
                elif prey_dist_array[i] == cur_prey_dist and pred_dist_array[i] > cur_pred_dist:
                    options[2].append(adjacent_nodes[i])
                elif prey_dist_array[i] == cur_prey_dist:
                    options[3].append(adjacent_nodes[i])
                elif pred_dist_array[i] > cur_pred_dist:
                    options[4].append(adjacent_nodes[i])
                elif pred_dist_array[i] == cur_pred_dist:
                    options[5].append(adjacent_nodes[i])
                else:
                    options[6].append(current_node.index)
            
            #randomly picks a choice if multiple good choices (could be optimized instead of picking randomly, but write up says randomly I believe)
            for result in options:
                if result:
                    result_index = random.choice(result)
                    break

            self.pos = result_index
            #returns 0 if moves into predator or predator moves into it
            if predator_pos == self.pos or not self.predator.move(self.environment,self.pos):
                return 0
            #returns 1 if moves into prey or prey moves into it
            if prey_pos == self.pos or not self.prey.move(self.environment,self.pos):
                return 1
        #returns -1 if timeout
        return -1
