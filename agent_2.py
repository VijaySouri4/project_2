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

        self.prey_predict_probability = np.zeros(50)
        self.prey_predict_probability[self.prey.pos] = 1

        self.pred_predict_probability = np.zeros(50)
        self.pred_predict_probability[self.prey.pos] = 1

    def update_probability(self, num, surveyed): 
        if surveyed == 1:
            return 0
        return (num) / (1 - surveyed) 

    def predict_prob(self, steps_in_future = 1):
        self.prey_predict_probability = np.zeros(50)
        self.prey_predict_probability[self.prey.pos] = 1

        for _ in range(steps_in_future):
            self.prey_predict_probability = np.dot(self.prey_predict_probability, self.environment.prey_trans_matrix)

        vfunction = np.vectorize(self.update_probability)       #apply update probabilty to the p vector
        self.prey_predict_probability = vfunction(self.prey_predict_probability, self.prey_predict_probability[self.pos])
        self.prey_predict_probability[self.pos] = 0

        """
        self.pred_predict_probability = np.zeros(50)
        self.pred_predict_probability[self.predator.pos] = 1

        predator_trans_matrix = np.zeros((50,50))
        for n in self.environment.lis:
            paths = self.environment.shortest_paths[n.index][self.pos][1]
            options_set = set()
            for i in paths:
                options_set.add(i[0])
            for option in options_set:
                num_options = len(options_set)
                predator_trans_matrix[n.index, option] += 1/num_options
                    
        self.pred_predict_probability = np.dot(self.pred_predict_probability, predator_trans_matrix)"""
        #self.self.pred_predict_probability = vfunction(self.self.pred_predict_probability, self.self.pred_predict_probability[self.pos])
        #self.self.pred_predict_probability[self.pos] = 0
        #TODO THE PROBABILITY IS DIFFERENT DEPENDING On next node duh

    """Movement function for agent 1
    returns 1 if catches prey, 0 if dies, -1 if timeout"""

    def move(self):
        #runs for 100 steps else returns false
        while self.steps <= 100:
            self.steps += 1
            actual_predator_pos = self.predator.pos
            actual_prey_pos = self.prey.pos
            predator_pos = actual_predator_pos #add to ignore when 1 away
            prey_pos = actual_prey_pos
            self.predict_prob()
            current_node = self.environment.lis[self.pos]
            shortest_paths = self.environment.shortest_paths
            if shortest_paths[self.pos][prey_pos] != 1:
                #array of possible choices
                adjacent_nodes = [current_node.left_node_index,
                current_node.right_node_index,
                current_node.other_node_index, self.pos] ## Corrected the adjacent_nodes. Previously there was only left_index, left_index and other_index. 

                #gets distances to predator from each direction
                avg_pred_dist = 0
                num_baseline = 0
                cur_pred_utility = shortest_paths[actual_predator_pos][self.pos]
                left_pred_utility = shortest_paths[actual_predator_pos][current_node.left_node_index] - cur_pred_utility
                right_pred_utility = shortest_paths[actual_predator_pos][current_node.right_node_index] - cur_pred_utility
                other_pred_utility = shortest_paths[actual_predator_pos][current_node.other_node_index] - cur_pred_utility
                cur_pred_utility = shortest_paths[actual_predator_pos][self.pos] - cur_pred_utility
                pred_utility_array = [left_pred_utility, right_pred_utility, other_pred_utility, cur_pred_utility]
                avg_pred_dist = shortest_paths[actual_predator_pos][self.pos] - 1
                """
                for pred_pos_index in range(len(self.pred_predict_probability)):
                    pred_pos_prob = self.pred_predict_probability[pred_pos_index]
                    if pred_pos_prob == 0:
                        continue
                    cur_pred_baseline = shortest_paths[pred_pos_index][self.pos][0]
                    avg_pred_dist += cur_pred_baseline
                    num_baseline += 1
                    left_pred_utility += (shortest_paths[pred_pos_index][current_node.left_node_index][0]) * pred_pos_prob
                    right_pred_utility += (shortest_paths[pred_pos_index][current_node.right_node_index][0]) * pred_pos_prob
                    if adjacent_nodes[2] != self.pos:
                        other_pred_utility += (shortest_paths[pred_pos_index][current_node.other_node_index][0]) * pred_pos_prob
                    cur_pred_utility += (shortest_paths[pred_pos_index][self.pos][0]) * pred_pos_prob
                avg_pred_dist /= num_baseline
                

                #puts distances from predator in array
                pred_utility_array = [left_pred_utility, right_pred_utility, other_pred_utility, cur_pred_utility]"""
                utility_array = [left_pred_utility, right_pred_utility, other_pred_utility, cur_pred_utility]
                
                left_prey_utility = 0
                right_prey_utility = 0
                other_prey_utility = 0
                cur_prey_utility = 0
                
                avg_prey_dist = 0
                num_baseline = 0
                for prey_pos_index in range(len(self.prey_predict_probability)):
                    prey_pos_prob = self.prey_predict_probability[prey_pos_index]
                    if prey_pos_prob == 0:
                        continue
                    cur_prey_baseline = shortest_paths[self.pos][prey_pos_index]
                    avg_prey_dist += cur_prey_baseline
                    num_baseline += 1

                    left_prey_utility += (cur_prey_baseline - shortest_paths[current_node.left_node_index][prey_pos_index]) * prey_pos_prob
                    right_prey_utility += (cur_prey_baseline - shortest_paths[current_node.right_node_index][prey_pos_index]) * prey_pos_prob
                    other_prey_utility += (cur_prey_baseline - shortest_paths[current_node.other_node_index][prey_pos_index]) * prey_pos_prob
                    cur_prey_utility += (cur_prey_baseline - shortest_paths[self.pos][prey_pos_index]) * prey_pos_prob
                avg_prey_dist /= num_baseline

                prey_utility_array = [left_prey_utility, right_prey_utility, other_prey_utility, cur_prey_utility]
                utility_array[0] = left_prey_utility + utility_array[0]
                utility_array[1] = right_prey_utility + utility_array[1]
                utility_array[2] = other_prey_utility + utility_array[2]
                
                
                if avg_pred_dist > avg_prey_dist:
                    highest_utility_list = np.where(np.isclose(prey_utility_array, np.amax(prey_utility_array)))[0]
                    self.pos = adjacent_nodes[random.choice(highest_utility_list)]
                if avg_pred_dist < 3:
                    highest_utility_list = np.where(np.isclose(pred_utility_array, np.amax(pred_utility_array)))[0]
                    self.pos = adjacent_nodes[random.choice(highest_utility_list)]
                else:
                    highest_utility_list = np.where(np.isclose(utility_array, np.amax(utility_array)))[0]
                    highest_utility_closest = np.array([prey_utility_array[x] for x in highest_utility_list])
                    indexes = [x for x in highest_utility_list]
                    self.pos = adjacent_nodes[indexes[random.choice(np.where(np.isclose(highest_utility_closest, np.amax(highest_utility_closest)))[0])]]
                
            else:
                if shortest_paths[current_node.left_node_index][prey_pos] == 0:
                    self.pos = current_node.left_node_index
                elif shortest_paths[current_node.right_node_index][prey_pos] == 0:
                    self.pos = current_node.right_node_index
                else:
                    self.pos = current_node.other_node_index
            #returns 0 if moves into predator or predator moves into it
            #print( self.pos, self.predator.pos, self.prey.pos)
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
