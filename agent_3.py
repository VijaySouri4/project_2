import random
import predator
import prey
import environment
import numpy as np
import get_optimal_node

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

        #make sure agent doesnt start in occupied node
        while self.prey.pos == self.pos or self.predator.pos == self.pos:
            self.pos = random.choice(range(0,49))

        prey_probability_array = [(1/49)] * 50
        prey_probability_array[self.pos] = 0
        self.prey_probability_array = np.array(prey_probability_array) #Belief array (sum of elements is 1)

        self.steps = 0

        #make sure agent doesnt start in occupied node
        while self.prey.pos == self.pos or self.predator.pos == self.pos:
            self.pos = random.choice(range(0,49))

        self.agent_steps = [self.pos]
        self.prey_steps = []
        self.predator_steps = [self.predator.pos]
        self.actual_prey_steps = [self.prey.pos]
        self.actual_predator_steps = [self.predator.pos]

        self.certain_prey_pos = 0

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
        while self.steps <= 5000:
            self.steps += 1
            predator_pos = self.predator.pos
            actual_prey_pos = self.prey.pos
            #survey highest probability node and return next highest probability node if survey false other wise one of four possible nodes if true
            prey_pos = self.survey()                          #not actual position just most likely

            if prey_pos == actual_prey_pos and np.isclose(self.prey_probability_array[prey_pos], 1):
                self.certain_prey_pos += 1
                
            if self.steps == 1:
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

            # get optimal node from the adjacent nodes.
            result_index = get_optimal_node.get(adjacent_nodes,prey_dist_array
            ,cur_prey_dist,pred_dist_array,cur_pred_dist)
            #Assign the optimal node index to agent's position

            self.pos = result_index
            self.predator_steps.append(self.predator.pos)
            self.prey_steps.append(prey_pos)
            self.actual_prey_steps.append(self.prey.pos)
            self.agent_steps.append(self.pos)
            self.actual_predator_steps.append(self.predator.pos)
            self.agent_moved()
            #returns 0 if moves into predator or predator moves into it
            if predator_pos == self.pos: 
                return 0, self.steps, self.agent_steps, self.prey_steps, self.predator_steps, self.actual_prey_steps, self.actual_predator_steps
            #returns 1 if moves into prey 
            if actual_prey_pos == self.pos:
                return 1, self.steps, self.agent_steps, self.prey_steps, self.predator_steps, self.actual_prey_steps, self.actual_predator_steps
            #returns 1 if prey moves into it
            if not self.prey.move(self.environment,self.pos):
                self.prey_steps.append(self.survey())
                self.actual_prey_steps.append(self.prey.pos)
                return 1, self.steps, self.agent_steps, self.prey_steps, self.predator_steps, self.actual_prey_steps, self.actual_predator_steps
            #returns 0 if predator moves into it
            if not self.predator.move(self.environment,self.pos):
                self.prey_steps.append(self.survey())
                self.actual_prey_steps.append(self.prey.pos)
                self.predator_steps.append(self.predator.pos)
                return 0, self.steps, self.agent_steps, self.prey_steps, self.predator_steps, self.actual_prey_steps, self.actual_predator_steps

            #update probabilites after movement (will only survey agents current pos not highest probability since True flag)
            self.transition()
            

        #returns -1 if timeout
        return -1, self.steps, self.agent_steps, self.prey_steps, self.predator_steps, self.actual_prey_steps, self.actual_predator_steps

def main(Verbose=False):
    count = 0
    for _ in range(1):
        ag = Agent_3()
        k = ag.move()
        if k[0] == 1:
            count += 1 
        print(k[0])
    print('---------------------------')
    print('Success count :' + str(count))
    if Verbose == True:
        print('Agent moves:')
        print(ag.agent_steps)
        print('Predicted Prey moves:')
        print(ag.prey_steps)
        print('Actual Prey moves:')
        print(ag.actual_prey_steps)
        print('Predator moves:')
        print(ag.predator_steps)
        print('Actual Predator moves:')
        print(ag.actual_predator_steps)
        print('Sizes of actual_prey, predicted_prey, predator and agent')
        print(len(ag.actual_prey_steps))
        print(len(ag.prey_steps))
        print(len(ag.predator_steps))
        print(len(ag.agent_steps))
        print(len(ag.actual_predator_steps))
if __name__ == '__main__':
    main(Verbose=True)
