import random
import predator
import prey
import environment
import numpy as np

class Agent_3:

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

        prey_probability_array = [(1/49)] * 50
        prey_probability_array[self.pos] = 0
        self.prey_probability_array = np.array(prey_probability_array)

        self.steps = 0

        #make sure agent doesnt start in occupied node
        while self.prey.pos == self.pos or self.predator.pos == self.pos:
            self.pos = random.choice(range(0,49))

    def update_probability(self, num, surveyed): 
        return (num) / (1 - surveyed)
    
    def survey(self, agent_move = False):   #if agent_move is true, use transition matrix to update probability (for when agent moves)
        if agent_move == True:  #on an agent move turn don't survey just set current agent pos to survey (always false) so it will get set to 0 and update probability
            choice = self.pos
        else:
            array = np.where(self.prey_probability_array == np.amax(self.prey_probability_array))[0] #most likely position is surveyed (random if multiple)
            choice = np.random.choice(array)
        if choice != self.prey.pos:     #if survey is false
            vfunction = np.vectorize(self.update_probability)       #apply update probabilty to the p vector
            self.prey_probability_array = vfunction(self.prey_probability_array, self.prey_probability_array[choice])
            self.prey_probability_array[choice] = 0

            if agent_move == True:  #if agent has moved, update probilities with transition matrix to guess prey movement
                self.prey_probability_array = np.dot(self.prey_probability_array, self.environment.trans_matrix)
                vfunction = np.vectorize(self.update_probability)
                self.prey_probability_array = vfunction(self.prey_probability_array, self.prey_probability_array[self.pos])
                self.prey_probability_array[self.pos] = 0
            #pick highest probability node and return it
            array = np.where(self.prey_probability_array == np.amax(self.prey_probability_array))[0]    #most likely position after removal of surveyed returned (random if multiple)
            choice = np.random.choice(array)
            return choice
        else:       #if the survey is true
            prey_node = self.environment.lis[choice]
            #all probabilites become false except the node of the prey and all adjacent to it
            self.prey_probability_array.fill(0)
            self.prey_probability_array[choice] = 1/4
            self.prey_probability_array[prey_node.right_node_index] = 1/4
            self.prey_probability_array[prey_node.left_node_index] = 1/4
            self.prey_probability_array[prey_node.other_node_index] = 1/4
            #pick highest probability node and return it
            array = np.where(self.prey_probability_array == np.amax(self.prey_probability_array))[0]    #most likely position after removal of surveyed returned (random if multiple)
            choice = np.random.choice(array)
            return choice 
            

    """Movement function for agent 1
    returns 1 if catches prey, 0 if dies, -1 if timeout"""

    def move(self):
        #runs for 100 steps else returns false
        while self.steps <= 100:
            self.steps += 1
            predator_pos = self.predator.pos
            actual_prey_pos = self.prey.pos
            #survey highest probability node and return next highest probability node if survey false other wise one of four possible nodes if true
            prey_pos = self.survey()                          #not actual position just most likely
            current_node = self.environment.lis[self.pos]
            shortest_paths = self.environment.shortest_paths

            
            #array of possible choices
            adjacent_nodes = [current_node.left_node_index,
            current_node.right_node_index,
            current_node.other_node_index] ## Corrected the adjacent_nodes. Previously there was only left_index, left_index and other_index. 

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
                if prey_dist_array[i] < cur_prey_dist and pred_dist_array[i] > cur_pred_dist:  ## Neighbors that are closer to the Prey and farther from the Predator
                    options[0].append(adjacent_nodes[i])
                elif prey_dist_array[i] < cur_prey_dist and not pred_dist_array[i] < cur_pred_dist:  ## Neighbors that are closer to the Prey and not closer to the Predator. # I beleive that we have to check that the chosen node is not closer to the predator here as priority 2
                    options[1].append(adjacent_nodes[i])
                elif prey_dist_array[i] == cur_prey_dist and pred_dist_array[i] > cur_pred_dist:
                    options[2].append(adjacent_nodes[i])
                elif prey_dist_array[i] == cur_prey_dist and not pred_dist_array[i] < cur_pred_dist:
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
            if predator_pos == self.pos: 
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

            #update probabilites after movement (will only survey agents current pos not highest probability since True flag)
            self.survey(True)
            

        #returns -1 if timeout
        return -1, self.steps
