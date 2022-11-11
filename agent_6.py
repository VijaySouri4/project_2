import random
import predator
import prey
import environment
import numpy as np

class Agent_6:

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

        self.steps = 0

        self.certain_predator_pos = 0

    #normalizes probability, uses sum since it is not just removing a probability
    def update_probability(self, num, prob_sum):
        if prob_sum == 0:
            return 0
        return (num) / (prob_sum) 
    
    def survey(self):   #if agent_move is true, use transition matrix to update probability (for when agent moves)
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

    def agent_moved(self):
        vfunction = np.vectorize(self.update_probability)
        self.predator_probability_array[self.pos] = 0
        self.predator_probability_array = vfunction(self.predator_probability_array, np.sum(self.predator_probability_array))

    def transition(self):

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

        vfunction = np.vectorize(self.update_probability)
                
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
        while self.steps <= 5000:
            self.steps += 1
            actual_predator_pos = self.predator.pos
            actual_prey_pos = self.prey.pos
            predator_pos = self.survey()  

            if predator_pos == actual_predator_pos and np.isclose(self.predator_probability_array[predator_pos], 1):
                self.certain_predator_pos += 1

            current_node = self.environment.lis[self.pos]
            shortest_paths = self.environment.shortest_paths

            adjacent_nodes = [current_node.left_node_index,
            current_node.right_node_index,
            current_node.other_node_index, self.pos]

            #Bellmans Eq for each of the possible routines (actions agent can take)

            if current_node.degree == 3:
                routine_left_predator_utility = np.sum((0.9 ** np.array([shortest_paths[current_node.left_node_index][node] for node in range(50)])) * self.predator_probability_array)
                routine_right_predator_utility = np.sum((0.9 ** np.array([shortest_paths[current_node.right_node_index][node] for node in range(50)])) * self.predator_probability_array)
                routine_cur_predator_utility = np.sum((0.9 ** np.array([shortest_paths[current_node.index][node] for node in range(50)])) * self.predator_probability_array)
                routine_other_predator_utility = np.sum((0.9 ** np.array([shortest_paths[current_node.other_node_index][node] for node in range(50)])) * self.predator_probability_array)
                predator_choices = np.array([routine_left_predator_utility, routine_right_predator_utility, routine_other_predator_utility, routine_cur_predator_utility])
            else:
                routine_left_predator_utility = np.sum((0.9 ** np.array([shortest_paths[current_node.left_node_index][node] for node in range(50)])) * self.predator_probability_array)
                routine_right_predator_utility = np.sum((0.9 ** np.array([shortest_paths[current_node.right_node_index][node] for node in range(50)])) * self.predator_probability_array)
                routine_cur_predator_utility = np.sum((0.9 ** np.array([shortest_paths[current_node.index][node] for node in range(50)])) * self.predator_probability_array)
                predator_choices = np.array([routine_left_predator_utility, routine_right_predator_utility, np.Infinity, routine_cur_predator_utility])

            if current_node.degree == 3:
                routine_left_prey_utility = 0.9 * (0.9 ** shortest_paths[current_node.left_node_index][actual_prey_pos])
                routine_right_prey_utility = 0.9 * (0.9 ** shortest_paths[current_node.right_node_index][actual_prey_pos])
                routine_cur_prey_utility = 0.9 * (0.9 ** shortest_paths[current_node.index][actual_prey_pos])
                routine_other_prey_utility = 0.9 * (0.9 ** shortest_paths[current_node.other_node_index][actual_prey_pos])
                prey_choices = np.array([routine_left_prey_utility, routine_right_prey_utility, routine_other_prey_utility, routine_cur_prey_utility])
            else:
                routine_left_prey_utility = 0.9 * (0.9 ** shortest_paths[current_node.left_node_index][actual_prey_pos])
                routine_right_prey_utility = 0.9 * (0.9 ** shortest_paths[current_node.right_node_index][actual_prey_pos])
                routine_cur_prey_utility = 0.9 * (0.9 ** shortest_paths[current_node.index][actual_prey_pos])
                prey_choices = np.array([routine_left_prey_utility, routine_right_prey_utility, 0, routine_cur_prey_utility])
            
            choices = prey_choices - predator_choices

            results =  np.where(np.isclose(choices, np.amax(choices)))[0]
            self.pos = adjacent_nodes[np.random.choice(results)]

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
