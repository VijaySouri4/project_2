import random
import predator
import prey
import environment
import numpy as np
import get_optimal_node
class Agent_7:

    def __init__(self, input_predator = None, input_prey = None, input_environment = None, input_pos = None) -> None:
        #Sets predator object if not specified
        if input_predator is None:
            self.predator = predator.Predator()
        else: 
            self.predator = input_predator
        #Sets prey object if not specified
        if input_prey is None:
            self.prey = prey.Prey()
        else:
            self.prey = input_prey
        #Sets environment if not specified
        if input_environment is None:
            self.environment = environment.Env(50)
        else:
            self.environment = input_environment

        #Sets agent position if not specified
        if input_pos is None:
            self.pos = random.choice(range(0,49))
        else:
            self.pos = input_pos

        self.steps = 0

        #make sure agent doesnt start in occupied node
        while self.prey.pos == self.pos or self.predator.pos == self.pos:
            self.pos = random.choice(range(0,49))

        #initilizes variables for animations
        self.agent_steps = [self.pos]
        self.prey_steps = []
        self.predator_steps = []
        self.actual_prey_steps = [self.prey.pos]
        self.actual_predator_steps = [self.predator.pos]
        
        #initilizes predator array to all zeros and 1 at predator position
        predator_probability_array = [0] * 50
        predator_probability_array[self.predator.pos] = 1
        self.predator_probability_array = np.array(predator_probability_array) #Belief array (sum of elements is 1)

        #initilizes prey array to 1/49 belief for all nodes
        prey_probability_array = [(1/49)] * 50
        prey_probability_array[self.pos] = 0
        self.prey_probability_array = np.array(prey_probability_array) #Belief array (sum of elements is 1)

        self.certain_prey_pos = 0
        self.certain_predator_pos = 0
        

    #normalizes probability
    def update_probability(self, num, prob_sum):
        if prob_sum == 0:
            return 0
        return (num) / (prob_sum) 

    """Function to handle surveying of a node and belief updates, returns highest belief predator and prey pos"""
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

    """Function to handle surveying of a node and belief updates, returns highest belief predator pos"""
    
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

    """Function to handle surveying of a node and belief updates, returns highest belief prey pos"""
        
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

    """Function to handle agent movement belief updates"""

    def agent_moved(self):
        vfunction = np.vectorize(self.update_probability)
        self.prey_probability_array[self.pos] = 0
        self.prey_probability_array = vfunction(self.prey_probability_array, np.sum(self.prey_probability_array)) 
        self.predator_probability_array[self.pos] = 0
        self.predator_probability_array = vfunction(self.predator_probability_array, np.sum(self.predator_probability_array))

    """Function to handle belief updates after actor movement (combines transition from partial prey and predator)"""

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
        while self.steps <= 5000:
            self.steps += 1
            actual_predator_pos = self.predator.pos
            actual_prey_pos = self.prey.pos
            #survey highest probability node and return next highest probability node if survey false other wise one of four possible nodes if true
            predator_pos, prey_pos = self.survey() #not actual position just most likely

            if prey_pos == actual_prey_pos and np.isclose(self.prey_probability_array[prey_pos], 1):
                self.certain_prey_pos += 1

            if predator_pos == actual_predator_pos and np.isclose(self.predator_probability_array[predator_pos], 1):
                self.certain_predator_pos += 1

            if self.steps == 1:
                self.predator_steps.append(predator_pos)
                self.prey_steps.append(prey_pos)                          
            current_node = self.environment.lis[self.pos]
            shortest_paths = self.environment.shortest_paths

            
            #array of possible choices
            adjacent_nodes = [current_node.left_node_index,
            current_node.right_node_index,
            current_node.other_node_index] ## Corrected the adjacent_nodes. Previously there was only left_index, left_index and other_index. 

            #gets distances to predator from each direction
            left_pred_dist = shortest_paths[current_node.left_node_index][predator_pos]
            right_pred_dist = shortest_paths[current_node.right_node_index][predator_pos]
            other_pred_dist = shortest_paths[current_node.other_node_index][predator_pos]
            cur_pred_dist = shortest_paths[self.pos][predator_pos]

            #puts distances from predator in array
            pred_dist_array = [left_pred_dist, right_pred_dist, other_pred_dist]

            #gets distances to prey from each direction
            left_prey_dist = shortest_paths[current_node.left_node_index][prey_pos]
            right_prey_dist = shortest_paths[current_node.right_node_index][prey_pos]
            other_prey_dist = shortest_paths[current_node.other_node_index][prey_pos]
            cur_prey_dist = shortest_paths[self.pos][prey_pos]

            #puts distances from prey in array
            prey_dist_array = [left_prey_dist, right_prey_dist, other_prey_dist]

            #Get the optimal node from the optimal node function
            result_index = get_optimal_node.get(adjacent_nodes,prey_dist_array
            ,cur_prey_dist,pred_dist_array,cur_pred_dist)
            #Assign the optimal node index to agent's position

            self.pos = result_index
            # The steps list help in animating the graph by timestep.
            self.predator_steps.append(predator_pos)
            self.actual_predator_steps.append(self.predator.pos)
            self.prey_steps.append(prey_pos)
            self.actual_prey_steps.append(self.prey.pos)
            self.agent_steps.append(self.pos)
            self.agent_moved()

            #returns 0 if moves into predator or predator moves into it
            if actual_predator_pos == self.pos: 
                return 0, self.steps, self.agent_steps, self.prey_steps, self.predator_steps, self.actual_prey_steps, self.actual_predator_steps
            #returns 1 if moves into prey 
            if actual_prey_pos == self.pos:
                return 1, self.steps, self.agent_steps, self.prey_steps, self.predator_steps, self.actual_prey_steps, self.actual_predator_steps
            #returns 1 if prey moves into it
            if not self.prey.move(self.environment,self.pos):
                predator_pos, prey_pos = self.survey()
                self.prey_steps.append(prey_pos)
                self.actual_prey_steps.append(self.prey.pos)
                return 1, self.steps, self.agent_steps, self.prey_steps, self.predator_steps, self.actual_prey_steps, self.actual_predator_steps
            #returns 0 if predator moves into it
            if not self.predator.move_distractable(self.environment,self.pos):
                predator_pos, prey_pos = self.survey()
                self.prey_steps.append(prey_pos)
                self.predator_steps.append(predator_pos)
                self.actual_prey_steps.append(self.prey.pos)
                self.actual_predator_steps.append(self.predator.pos)
                return 0, self.steps, self.agent_steps, self.prey_steps, self.predator_steps, self.actual_prey_steps, self.actual_predator_steps

            #update probabilites after movement (will only survey agents current pos not highest probability since True flag)
            self.transition()
            

        #returns -1 if timeout
        return -1, self.steps, self.agent_steps, self.prey_steps, self.predator_steps, self.actual_prey_steps, self.actual_predator_steps

def main(Verbose=False):
    count = 0
    rangee = 1
    for _ in range(rangee):
        ag = Agent_7()
        k = ag.move()
        if k[0] == 1:
            count += 1 
        #print(k[0])
    print('---------------------------')
    print('Success count :' + str((count/rangee)*100))
    if Verbose == True:
        print('Agent moves:')
        print(ag.agent_steps)
        print('Beleived Prey moves:')
        print(ag.prey_steps)
        print('Actual Prey moves:')
        print(ag.actual_prey_steps)
        print('Believed Predator moves:')
        print(ag.predator_steps)
        print('Actual Predator moves:')
        print(ag.actual_predator_steps)
        print('pred, predy and agent last steps')
        print(ag.predator.pos)
        print(ag.prey.pos)
        print(ag.pos)
        
        print('Size of actual_prey'+str(len(ag.actual_prey_steps)))
        print('Size of predicted prey'+str(len(ag.prey_steps)))
        print('Size of predicted predator'+str(len(ag.predator_steps)))
        print('Size of agent'+str(len(ag.agent_steps)))
        print('Size of actual predator'+str(len(ag.actual_predator_steps)))
if __name__ == '__main__':
    main(Verbose=True)
