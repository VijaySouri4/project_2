import random
import predator
import prey
import environment
import numpy as np

class Agent_4:

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

        prey_probability_array = [(1/49)] * 50
        prey_probability_array[self.pos] = 0
        self.prey_probability_array = np.array(prey_probability_array) #Belief array (sum of elements is 1)

        self.steps = 0

        

    #normalizes probability
    def update_probability(self, num, prob_sum):
        if prob_sum == 0:
            return 0
        return (num) / (prob_sum) 
    
    def survey(self):   #if agent_move is true, use transition matrix to update probability (for when agent moves)
        array = np.where(np.isclose(self.prey_probability_array, np.amax(self.prey_probability_array)))[0] #most likely position is surveyed (random if multiple)
        choice = np.random.choice(array)

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
        
    def transition(self):
        vfunction = np.vectorize(self.update_probability)
        self.prey_probability_array = np.dot(self.prey_probability_array, self.environment.prey_trans_matrix)
        self.prey_probability_array[self.pos] = 0
        self.prey_probability_array = vfunction(self.prey_probability_array, np.sum(self.prey_probability_array))   

    """Movement function for agent 1
    returns 1 if catches prey, 0 if dies, -1 if timeout"""

    def move(self):
        #runs for 100 steps else returns false
        while self.steps < 100:
            actual_predator_pos = self.predator.pos
            actual_prey_pos = self.prey.pos
            self.survey()
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
                routine_left_prey_utility = np.sum((0.9 ** np.array([shortest_paths[current_node.left_node_index][node] for node in range(50)])) * self.prey_probability_array)
                routine_right_prey_utility = np.sum((0.9 ** np.array([shortest_paths[current_node.right_node_index][node] for node in range(50)])) * self.prey_probability_array)
                routine_cur_prey_utility = np.sum((0.9 ** np.array([shortest_paths[current_node.index][node] for node in range(50)])) * self.prey_probability_array)
                routine_other_prey_utility = np.sum((0.9 ** np.array([shortest_paths[current_node.other_node_index][node] for node in range(50)])) * self.prey_probability_array)
                prey_choices = np.array([routine_left_prey_utility, routine_right_prey_utility, routine_other_prey_utility, routine_cur_prey_utility])
            else:
                routine_left_prey_utility = np.sum((0.9 ** np.array([shortest_paths[current_node.left_node_index][node] for node in range(50)])) * self.prey_probability_array)
                routine_right_prey_utility = np.sum((0.9 ** np.array([shortest_paths[current_node.right_node_index][node] for node in range(50)])) * self.prey_probability_array)
                routine_cur_prey_utility = np.sum((0.9 ** np.array([shortest_paths[current_node.index][node] for node in range(50)])) * self.prey_probability_array)
                prey_choices = np.array([routine_left_prey_utility, routine_right_prey_utility, 0, routine_cur_prey_utility])
            
            choices = prey_choices - predator_choices

            results =  np.where(np.isclose(choices, np.amax(choices)))[0]
            
            self.pos = adjacent_nodes[np.random.choice(results)]
            self.steps += 1

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
            if not self.predator.move(self.environment,self.pos):
                return 0, self.steps
                
            #update probabilites after movement (will only survey agents current pos not highest probability since True flag)
            self.transition()

        #returns -1 if timeout
        return -1, self.steps
