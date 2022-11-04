import random
import predator
import prey
import environment
import numpy as np
class Agent_8:

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

        #make sure agent doesnt start in occupied node
        while self.prey.pos == self.pos or self.predator.pos == self.pos:
            self.pos = random.choice(range(0,49))

        predator_probability_array = [0] * 50
        predator_probability_array[self.predator.pos] = 1
        self.predator_probability_array = np.array(predator_probability_array) #Belief array (sum of elements is 1)

        prey_probability_array = [(1/49)] * 50
        prey_probability_array[self.pos] = 0
        self.prey_probability_array = np.array(prey_probability_array) #Belief array (sum of elements is 1)

        self.steps = 0

    #normalizes probability
    def update_probability(self, num, prob_sum):
        if prob_sum == 0:
            return 0
        return (num) / (prob_sum) 

    #combined surveys for prey and predator
    def survey(self):
        
        if np.isclose(np.amax(self.predator_probability_array), 1):
            #print("Agent pos", self.pos, "| Pred pos", self.predator.pos, " | Most Likely Pred Pos", np.where(self.predator_probability_array == np.amax(self.predator_probability_array))[0], " | Probability", np.amax(self.predator_probability_array))
            array = np.where(np.isclose(self.prey_probability_array, np.amax(self.prey_probability_array)))[0] #most likely position is surveyed (random if multiple)
            choice = np.random.choice(array)
        else:
            array = np.where(np.isclose(self.predator_probability_array, np.amax(self.predator_probability_array)))[0] #most likely position is surveyed (random if multiple)
            ties = []
            closest = np.Infinity
            for index in array:
                if self.environment.shortest_paths[index][self.pos] < closest:
                    closest = self.environment.shortest_paths[index][self.pos]
                    ties = [index]
                elif self.environment.shortest_paths[index][self.pos] == closest:
                    closest = self.environment.shortest_paths[index][self.pos]
                    ties.append(index)
            choice = np.random.choice(ties)
            
            
        return self.predator_survey(choice), self.prey_survey(choice)
    
    def predator_survey(self, choice = None):   #if agent_move is true, use transition matrix to update probability (for when agent moves)
        if choice != self.predator.pos:     #if survey is false (or agent moved and lived)
            vfunction = np.vectorize(self.update_probability)     #apply update probabilty to the p vector
            self.predator_probability_array[choice] = 0
            self.predator_probability_array = vfunction(self.predator_probability_array, np.sum(self.predator_probability_array))

            array = np.where(np.isclose(self.predator_probability_array, np.amax(self.predator_probability_array)))[0]
            ties = []
            closest = np.Infinity
            for index in array:
                if self.environment.shortest_paths[index][self.pos] < closest:
                    closest = self.environment.shortest_paths[index][self.pos]
                    ties = [index]
                elif self.environment.shortest_paths[index][self.pos] == closest:
                    closest = self.environment.shortest_paths[index][self.pos]
                    ties.append(index)
            choice = np.random.choice(ties)

        else:       #if the survey is true
            #sets all probabilites to zero except the potential next paths of predator
            self.predator_probability_array.fill(0)
            self.predator_probability_array[choice] = 1
        return choice
        
    def prey_survey(self, choice = None):   #if agent_move is true, use transition matrix to update probability (for when agent moves)
        if choice != self.prey.pos:     #if survey is false
            vfunction = np.vectorize(self.update_probability)       #apply update probabilty to the p vector
            self.prey_probability_array[choice] = 0
            self.prey_probability_array = vfunction(self.prey_probability_array, np.sum(self.prey_probability_array))

            #pick highest probability node and return it
            array = np.where(np.isclose(self.prey_probability_array, np.amax(self.prey_probability_array)))[0]    #most likely position after removal of surveyed returned (random if multiple)
            choice = np.random.choice(array)
        else:       #if the survey is true

            #all probabilites become false except the node of the prey and all adjacent to it
            self.prey_probability_array.fill(0)
            self.prey_probability_array[choice] = 1
        return choice

    def agent_moved(self):
        vfunction = np.vectorize(self.update_probability)
        self.prey_probability_array[self.pos] = 0
        self.prey_probability_array = vfunction(self.prey_probability_array, np.sum(self.prey_probability_array))
        self.predator_probability_array[self.pos] = 0
        self.predator_probability_array = vfunction(self.predator_probability_array, np.sum(self.predator_probability_array))    

    def transition(self):

        vfunction = np.vectorize(self.update_probability)
        #Prey Transition
        self.prey_probability_array = np.dot(self.prey_probability_array, self.environment.prey_trans_matrix)
        self.prey_probability_array[self.pos] = 0
        self.prey_probability_array = vfunction(self.prey_probability_array, np.sum(self.prey_probability_array)) 

        #Predator Transition
        predator_trans_matrix = np.zeros((50,50))
        #build focused predator matrix
        for n in self.environment.lis:
            if n.degree == 2:
                options = np.array([n.index, n.left_node_index,  n.right_node_index])
                option_distances = [self.environment.shortest_paths[n.index][self.pos], 
                self.environment.shortest_paths[n.left_node_index][self.pos],  
                self.environment.shortest_paths[n.right_node_index][self.pos]]
            else:
                options = np.array([n.index, n.left_node_index,  n.right_node_index,  n.other_node_index])
                option_distances = np.array([self.environment.shortest_paths[n.index][self.pos], 
                self.environment.shortest_paths[n.left_node_index][self.pos],  
                self.environment.shortest_paths[n.right_node_index][self.pos],  
                self.environment.shortest_paths[n.other_node_index][self.pos]])
            options_list = np.where(np.isclose(option_distances, np.amin(option_distances)))[0] #shortest next paths
            for option_index in options_list:
                option = options[option_index]
                num_options = len(options_list)
                predator_trans_matrix[n.index, option] += 1/num_options
                    
        focused_predator_vector = self.predator_probability_array.copy()
        focused_predator_vector = np.dot(focused_predator_vector, predator_trans_matrix)

        distracted_predator_vector = self.predator_probability_array.copy()
        distracted_predator_vector = np.dot(distracted_predator_vector, self.environment.distracted_trans_matrix)

        self.predator_probability_array = distracted_predator_vector * 0.4 + focused_predator_vector * 0.6
        self.predator_probability_array =  vfunction(self.predator_probability_array, np.sum(self.predator_probability_array))

        self.predator_probability_array[self.pos] = 0
        self.predator_probability_array =  vfunction(self.predator_probability_array, np.sum(self.predator_probability_array))
                
            
    """Movement function for agent 1
    returns 1 if catches prey, 0 if dies, -1 if timeout"""

    def move(self):
        #runs for 100 steps else returns false
        while self.steps <= 100:
            self.steps += 1
            actual_predator_pos = self.predator.pos
            actual_prey_pos = self.prey.pos
            #survey highest probability node and return next highest probability node if survey false other wise one of four possible nodes if true
            predator_pos, prey_pos = self.survey()                          #not actual position just most likely
            current_node = self.environment.lis[self.pos]
            shortest_paths = self.environment.shortest_paths

            #if not adjacent to prey
            if shortest_paths[self.pos][prey_pos] != 1:
                #List of all nodes adjacent nodes to agent
                adjacent_nodes = [current_node.left_node_index,
                current_node.right_node_index,
                current_node.other_node_index, self.pos]

                #gets distances to predator from each direction and subtracts 1 to get dist for next step, calculates utility based off the dist of current node being 0
                cur_pred_utility = shortest_paths[predator_pos][self.pos] - 1
                left_pred_utility = shortest_paths[predator_pos][current_node.left_node_index] - 1 - cur_pred_utility
                right_pred_utility = shortest_paths[predator_pos][current_node.right_node_index] - 1 - cur_pred_utility
                if current_node.degree == 3:
                    other_pred_utility = shortest_paths[predator_pos][current_node.other_node_index] - 1 - cur_pred_utility
                    avg_pred_dist = (shortest_paths[predator_pos][self.pos] - 1 + 
                        shortest_paths[predator_pos][current_node.left_node_index] - 1 + 
                        shortest_paths[predator_pos][current_node.right_node_index] - 1 + 
                        shortest_paths[predator_pos][current_node.other_node_index] - 1) / 4
                else:
                    other_pred_utility = np.NINF
                    avg_pred_dist = (shortest_paths[predator_pos][self.pos] - 1 + 
                        shortest_paths[predator_pos][current_node.left_node_index] - 1 + 
                        shortest_paths[predator_pos][current_node.right_node_index] - 1) / 3
                cur_pred_utility = shortest_paths[predator_pos][self.pos]- 1 - cur_pred_utility

                pred_utility_array = [left_pred_utility, right_pred_utility, other_pred_utility, cur_pred_utility] 
                
                left_prey_utility = 0
                right_prey_utility = 0
                other_prey_utility = 0
                cur_prey_utility = 0
                
                #determine the avg distance from each node agent to move to to the possible nodes the prey can move to
                #normalize these values to utility by basing the current position as 0
                avg_prey_dist = 0
                prey_node = self.environment.lis[prey_pos]
                if prey_node.degree == 2:
                    prey_adjacent_nodes = [prey_node.index, prey_node.left_node_index,  prey_node.right_node_index]
                else:
                    prey_adjacent_nodes = [prey_node.index, prey_node.left_node_index,  prey_node.right_node_index,  prey_node.other_node_index]
                
                for prey_pos_index in prey_adjacent_nodes:
                    cur_prey_baseline = shortest_paths[self.pos][prey_pos_index]
                    avg_prey_dist += cur_prey_baseline

                    left_prey_utility += (cur_prey_baseline - shortest_paths[current_node.left_node_index][prey_pos_index]) / len(prey_adjacent_nodes)
                    right_prey_utility += (cur_prey_baseline - shortest_paths[current_node.right_node_index][prey_pos_index]) / len(prey_adjacent_nodes)
                    other_prey_utility += (cur_prey_baseline - shortest_paths[current_node.other_node_index][prey_pos_index]) / len(prey_adjacent_nodes)
                    cur_prey_utility += (cur_prey_baseline - shortest_paths[self.pos][prey_pos_index]) / len(prey_adjacent_nodes)
                avg_prey_dist /= len(prey_adjacent_nodes)

                prey_utility_array = [left_prey_utility, right_prey_utility, other_prey_utility, cur_prey_utility]

                #create combined utility array
                utility_array = [[] for _ in range(4)]
                utility_array[0] = left_prey_utility + pred_utility_array[0]
                utility_array[1] = right_prey_utility + pred_utility_array[1]
                utility_array[2] = other_prey_utility + pred_utility_array[2]
                utility_array[3] = other_prey_utility + pred_utility_array[3]
                
                #If closer to prey than predator, only focus on prey utility
                #If close to predator, run away (may time out but prevents death)
                #if closish to predator, find combined utility
                """if avg_pred_dist > avg_prey_dist:
                    highest_utility_list = np.where(np.isclose(prey_utility_array, np.amax(prey_utility_array)))[0]
                    self.pos = adjacent_nodes[random.choice(highest_utility_list)]"""
                if avg_pred_dist < 3:
                    highest_utility_list = np.where(np.isclose(pred_utility_array, np.amax(pred_utility_array)))[0]
                    self.pos = adjacent_nodes[random.choice(highest_utility_list)]
                else:
                    highest_utility_list = np.where(np.isclose(utility_array, np.amax(utility_array)))[0]
                    highest_utility_closest = np.array([prey_utility_array[x] for x in highest_utility_list])
                    indexes = [x for x in highest_utility_list]
                    self.pos = adjacent_nodes[indexes[random.choice(np.where(np.isclose(highest_utility_closest, np.amax(highest_utility_closest)))[0])]]
                
            else:
                #if right next to prey go to prey
                if shortest_paths[current_node.left_node_index][prey_pos] == 0:
                    self.pos = current_node.left_node_index
                elif shortest_paths[current_node.right_node_index][prey_pos] == 0:
                    self.pos = current_node.right_node_index
                else:
                    self.pos = current_node.other_node_index

            self.agent_moved()

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
            if not self.predator.move_distractable(self.environment,self.pos):
                return 0, self.steps

            #update probabilites after movement (will only survey agents current pos not highest probability since True flag)
            self.transition()
            

        #returns -1 if timeout
        return -1, self.steps
