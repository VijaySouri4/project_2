import random
import predator
import prey
import environment

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
            self.steps += 1

            #gets the most likely next position of the predator
            dist, path = self.environment.shortest_paths[self.predator.pos][self.pos]
            #sets value to next position of predator unless the next position is the agents position
            if dist != 0:
                predator_next_pos = path[0]
            else:
                predator_next_pos = self.predator.pos

            #sets value to furthest possible position of prey in next move
            longest_prey_dist = -1
            options = [self.environment.lis[self.prey.pos].index, 
            self.environment.lis[self.prey.pos].left_node_index,  
            self.environment.lis[self.prey.pos].right_node_index,  
            self.environment.lis[self.prey.pos].other_node_index]

            results = []
            for i in options:
                dist, path = self.environment.shortest_paths[self.prey.pos][self.pos]
                if longest_prey_dist < dist:
                    results = [path[0]]
                elif longest_prey_dist == dist:
                    results.append(path[0])
            prey_next_pos = random.choice(results)

            current_node = self.environment.lis[self.pos]
            shortest_paths = self.environment.shortest_paths

            #array of possible choices
            adjacent_nodes = [current_node.left_node_index,
            current_node.left_node_index,
            current_node.other_node_index]

            #gets distances to predator from each direction
            left_pred_dist = shortest_paths[current_node.left_node_index][predator_next_pos][0]
            right_pred_dist = shortest_paths[current_node.right_node_index][predator_next_pos][0]
            other_pred_dist = shortest_paths[current_node.other_node_index][predator_next_pos][0]
            cur_pred_dist = shortest_paths[self.pos][predator_next_pos][0]

            #puts distances from predator in array
            pred_dist_array = [left_pred_dist, right_pred_dist, other_pred_dist]

            #gets distances to prey from each direction
            left_prey_dist = shortest_paths[current_node.left_node_index][prey_next_pos ][0]
            right_prey_dist = shortest_paths[current_node.right_node_index][prey_next_pos ][0]
            other_prey_dist = shortest_paths[current_node.other_node_index][prey_next_pos ][0]
            cur_prey_dist = shortest_paths[self.pos][prey_next_pos ][0]

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
            if self.predator.pos == self.pos or not self.predator.move(self.environment,self.pos):
                return 0
            #returns 1 if moves into prey or prey moves into it
            if self.prey.pos == self.pos or not self.prey.move(self.environment,self.pos):
                return 1
        #returns -1 if timeout
        return -1
