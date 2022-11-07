from itertools import cycle
import random
import predator
import prey
import environment

class Agent_1:

    def __init__(self, input_predator = None, input_prey = None, input_environment = None, input_pos = None, verbose = False) -> None:
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

        self.agent_steps = [self.pos]
        self.prey_steps = [self.prey.pos]
        self.predator_steps = [self.prey.pos]

    """Movement function for agent 1
    returns 1 if catches prey, 0 if dies, -1 if timeout"""

    def move(self):
        #runs for 50 steps else returns false
        while self.steps <= 50:
            self.steps += 1
            predator_pos = self.predator.pos
            
            prey_pos = self.prey.pos

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

            '''
            -Neighbors that are closer to the Prey and farther from the Predator.
            -Neighbors that are closer to the Prey and not closer to the Predator.
            -Neighbors that are not farther from the Prey and farther from the Predator.
            -Neighbors that are not farther from the Prey and not closer to the Predator.
            -Neighbors that are farther from the Predator.
            -Neighbors that are not closer to the Predator.
            -Sit still and pray.
            '''

            ## Find nodes that satisfy priority 1, --> Neighbors that are closer to the Prey and farther from the Predator.
            #This means that the neighbor node should be closer to the prey and also farther from the predator
            priority1 = []
            optimal_adjascent_node = adjacent_nodes[0]
            optimal_prey_distance = prey_dist_array[0]
            optimal_pred_distance = pred_dist_array[0]

            priority2 = []
            priority3 = []
            priority4 = []
            priority5 = []
            priority6 = []
            cycle_flag = 0
            for k,i in enumerate(adjacent_nodes):
                #print('i value:'+str(i))
                if prey_dist_array[k] < cur_prey_dist and pred_dist_array[k] > cur_pred_dist:
                    priority1.append(i)
                    # For each of the selected node, check the same 6 conditions to get the best move
                    # The cycle flag variable ensures that a lower priority adjacent node does not overwrite the higher priority node.
                    if prey_dist_array[k] < optimal_prey_distance and pred_dist_array[k] > optimal_pred_distance:
                        optimal_adjascent_node = i
                        optimal_prey_distance = prey_dist_array[k]
                        optimal_pred_distance = pred_dist_array[k]
                        cycle_flag += 1
                    elif prey_dist_array[k] < optimal_prey_distance and not pred_dist_array[k] < optimal_pred_distance:
                        optimal_adjascent_node = i
                        optimal_prey_distance = prey_dist_array[k]
                        optimal_pred_distance = pred_dist_array[k]
                        cycle_flag += 1
                    elif not prey_dist_array[k] > optimal_prey_distance and pred_dist_array[k] > optimal_pred_distance:
                        optimal_adjascent_node = i
                        optimal_prey_distance = prey_dist_array[k]
                        optimal_pred_distance = pred_dist_array[k]
                        cycle_flag += 1
                    elif not prey_dist_array[k] > optimal_prey_distance and not pred_dist_array[k] < optimal_pred_distance:
                        optimal_adjascent_node = i
                        optimal_prey_distance = prey_dist_array[k]
                        optimal_pred_distance = pred_dist_array[k]
                        cycle_flag += 1
                    elif pred_dist_array[k] > optimal_pred_distance:
                        optimal_adjascent_node = i
                        optimal_prey_distance = prey_dist_array[k]
                        optimal_pred_distance = pred_dist_array[k]
                        cycle_flag += 1
                    elif not pred_dist_array[k] < optimal_pred_distance:
                        optimal_adjascent_node = i
                        optimal_prey_distance = prey_dist_array[k]
                        optimal_pred_distance = pred_dist_array[k]
                        cycle_flag += 1
                ## Prioirty2 --> Neighbors that are closer to the Prey and not closer to the Predator.
                # This means that the new node should be closer to the prey but need not be farther from the predator, so kinda like >=

                elif prey_dist_array[k] < cur_prey_dist and pred_dist_array[k] >= cur_pred_dist:
                    priority2.append(i)

                    if prey_dist_array[k] < optimal_prey_distance and pred_dist_array[k] > optimal_pred_distance and not cycle_flag > 0:
                        optimal_adjascent_node = i
                        optimal_prey_distance = prey_dist_array[k]
                        optimal_pred_distance = pred_dist_array[k]
                        cycle_flag += 1
                    elif prey_dist_array[k] < optimal_prey_distance and not pred_dist_array[k] < optimal_pred_distance and not cycle_flag > 0:
                        optimal_adjascent_node = i
                        optimal_prey_distance = prey_dist_array[k]
                        optimal_pred_distance = pred_dist_array[k]
                        cycle_flag += 1
                    elif not prey_dist_array[k] > optimal_prey_distance and pred_dist_array[k] > optimal_pred_distance and not cycle_flag > 0:
                        optimal_adjascent_node = i
                        optimal_prey_distance = prey_dist_array[k]
                        optimal_pred_distance = pred_dist_array[k]
                        cycle_flag += 1
                    elif not prey_dist_array[k] > optimal_prey_distance and not pred_dist_array[k] < optimal_pred_distance and not cycle_flag > 0:
                        optimal_adjascent_node = i
                        optimal_prey_distance = prey_dist_array[k]
                        optimal_pred_distance = pred_dist_array[k]
                        cycle_flag += 1
                    elif pred_dist_array[k] > optimal_pred_distance and not cycle_flag > 0:
                        optimal_adjascent_node = i
                        cycle_flag += 1
                        optimal_prey_distance = prey_dist_array[k]
                        optimal_pred_distance = pred_dist_array[k]
                        cycle_flag += 1
                    elif not pred_dist_array[k] < optimal_pred_distance and not cycle_flag > 0:
                        optimal_adjascent_node = i
                        cycle_flag += 1
                        optimal_prey_distance = prey_dist_array[k]
                        optimal_pred_distance = pred_dist_array[k]
                        cycle_flag += 1

                elif not prey_dist_array[k] > cur_prey_dist and pred_dist_array[k] > cur_pred_dist:
                    priority3.append(i)

                    if prey_dist_array[k] < optimal_prey_distance and pred_dist_array[k] > optimal_pred_distance and not cycle_flag > 0:
                        optimal_adjascent_node = i
                        optimal_prey_distance = prey_dist_array[k]
                        optimal_pred_distance = pred_dist_array[k]
                        cycle_flag += 1
                    elif prey_dist_array[k] < optimal_prey_distance and not pred_dist_array[k] < optimal_pred_distance and not cycle_flag > 0:
                        optimal_adjascent_node = i
                        optimal_prey_distance = prey_dist_array[k]
                        optimal_pred_distance = pred_dist_array[k]
                        cycle_flag += 1
                    elif not prey_dist_array[k] > optimal_prey_distance and pred_dist_array[k] > optimal_pred_distance and not cycle_flag > 0:
                        optimal_adjascent_node = i
                        optimal_prey_distance = prey_dist_array[k]
                        optimal_pred_distance = pred_dist_array[k]
                        cycle_flag += 1
                    elif not prey_dist_array[k] > optimal_prey_distance and not pred_dist_array[k] < optimal_pred_distance and not cycle_flag > 0:
                        optimal_adjascent_node = i
                        optimal_prey_distance = prey_dist_array[k]
                        optimal_pred_distance = pred_dist_array[k]
                        cycle_flag += 1
                    elif pred_dist_array[k] > optimal_pred_distance and not cycle_flag > 0:
                        optimal_adjascent_node = i
                        optimal_prey_distance = prey_dist_array[k]
                        optimal_pred_distance = pred_dist_array[k]
                        cycle_flag += 1
                    elif not pred_dist_array[k] < optimal_pred_distance and not cycle_flag > 0:
                        optimal_adjascent_node = i
                        optimal_prey_distance = prey_dist_array[k]
                        optimal_pred_distance = pred_dist_array[k]
                        cycle_flag += 1

                elif not prey_dist_array[k] > cur_prey_dist and not pred_dist_array[k] < cur_pred_dist:
                    priority4.append(i)

                    if prey_dist_array[k] < optimal_prey_distance and pred_dist_array[k] > optimal_pred_distance and not cycle_flag > 0:
                        optimal_adjascent_node = i
                        optimal_prey_distance = prey_dist_array[k]
                        optimal_pred_distance = pred_dist_array[k]
                    elif prey_dist_array[k] < optimal_prey_distance and not pred_dist_array[k] < optimal_pred_distance and not cycle_flag > 0:
                        optimal_adjascent_node = i
                        optimal_prey_distance = prey_dist_array[k]
                        optimal_pred_distance = pred_dist_array[k]
                    elif not prey_dist_array[k] > optimal_prey_distance and pred_dist_array[k] > optimal_pred_distance and not cycle_flag > 0:
                        optimal_adjascent_node = i
                    elif not prey_dist_array[k] > optimal_prey_distance and not pred_dist_array[k] < optimal_pred_distance and not cycle_flag > 0:
                        optimal_adjascent_node = i
                        optimal_prey_distance = prey_dist_array[k]
                        optimal_pred_distance = pred_dist_array[k]
                        cycle_flag += 1
                    elif pred_dist_array[k] > optimal_pred_distance and not cycle_flag > 0:
                        optimal_adjascent_node = i
                        optimal_prey_distance = prey_dist_array[k]
                        optimal_pred_distance = pred_dist_array[k]
                        cycle_flag += 1
                    elif not pred_dist_array[k] < optimal_pred_distance and not cycle_flag > 0:
                        optimal_adjascent_node = i
                        optimal_prey_distance = prey_dist_array[k]
                        optimal_pred_distance = pred_dist_array[k]
                        cycle_flag += 1

                elif pred_dist_array[k] > cur_pred_dist:
                    priority5.append(i)

                    if prey_dist_array[k] < optimal_prey_distance and pred_dist_array[k] > optimal_pred_distance and not cycle_flag > 0:
                        optimal_adjascent_node = i
                        optimal_prey_distance = prey_dist_array[k]
                        optimal_pred_distance = pred_dist_array[k]
                    elif prey_dist_array[k] < optimal_prey_distance and not pred_dist_array[k] < optimal_pred_distance and not cycle_flag > 0:
                        optimal_adjascent_node = i
                        optimal_prey_distance = prey_dist_array[k]
                        optimal_pred_distance = pred_dist_array[k]
                    elif not prey_dist_array[k] > optimal_prey_distance and pred_dist_array[k] > optimal_pred_distance and not cycle_flag > 0:
                        optimal_adjascent_node = i
                        optimal_prey_distance = prey_dist_array[k]
                        optimal_pred_distance = pred_dist_array[k]
                    elif not prey_dist_array[k] > optimal_prey_distance and not pred_dist_array[k] < optimal_pred_distance and not cycle_flag > 0:
                        optimal_adjascent_node = i
                        optimal_prey_distance = prey_dist_array[k]
                        optimal_pred_distance = pred_dist_array[k]
                        cycle_flag += 1
                    elif pred_dist_array[k] > optimal_pred_distance and not cycle_flag > 0:
                        optimal_adjascent_node = i
                        optimal_prey_distance = prey_dist_array[k]
                        optimal_pred_distance = pred_dist_array[k]
                        cycle_flag += 1
                    elif not pred_dist_array[k] < optimal_pred_distance and not cycle_flag > 0:
                        optimal_adjascent_node = i
                        optimal_prey_distance = prey_dist_array[k]
                        optimal_pred_distance = pred_dist_array[k]
                        cycle_flag += 1

                elif not pred_dist_array[k] < cur_pred_dist:
                    priority6.append(i)

                    if prey_dist_array[k] < optimal_prey_distance and pred_dist_array[k] > optimal_pred_distance and not cycle_flag > 0:
                        optimal_adjascent_node = i
                        optimal_prey_distance = prey_dist_array[k]
                        optimal_pred_distance = pred_dist_array[k]
                    elif prey_dist_array[k] < optimal_prey_distance and not pred_dist_array[k] < optimal_pred_distance and not cycle_flag > 0:
                        optimal_adjascent_node = i
                        optimal_prey_distance = prey_dist_array[k]
                        optimal_pred_distance = pred_dist_array[k]
                    elif not prey_dist_array[k] > optimal_prey_distance and pred_dist_array[k] > optimal_pred_distance and not cycle_flag > 0:
                        optimal_adjascent_node = i
                        optimal_prey_distance = prey_dist_array[k]
                        optimal_pred_distance = pred_dist_array[k]
                    elif not prey_dist_array[k] > optimal_prey_distance and not pred_dist_array[k] < optimal_pred_distance and not cycle_flag > 0:
                        optimal_adjascent_node = i
                        optimal_prey_distance = prey_dist_array[k]
                        optimal_pred_distance = pred_dist_array[k]
                        cycle_flag += 1
                    elif pred_dist_array[k] > optimal_pred_distance and not cycle_flag > 0:
                        optimal_adjascent_node = i
                        optimal_prey_distance = prey_dist_array[k]
                        optimal_pred_distance = pred_dist_array[k]
                        cycle_flag += 1
                    elif not pred_dist_array[k] < optimal_pred_distance and not cycle_flag > 0:
                        optimal_adjascent_node = i
                        optimal_prey_distance = prey_dist_array[k]
                        optimal_pred_distance = pred_dist_array[k]
                        cycle_flag += 1
            
            result_index = optimal_adjascent_node
            self.pos = result_index

            self.predator_steps.append(self.predator.pos)
            self.prey_steps.append(self.prey.pos)
            self.agent_steps.append(self.pos)
            #returns 0 if moves into predator or predator moves into it
            if predator_pos == self.pos: 
                return 0, self.steps, self.agent_steps, self.prey_steps, self.predator_steps
            #returns 1 if moves into prey 
            if prey_pos == self.pos:
                return 1, self.steps, self.agent_steps, self.prey_steps, self.predator_steps
            #returns 1 if prey moves into it
            if not self.prey.move(self.environment,self.pos):
                self.prey_steps.append(self.prey.pos)
                return 1, self.steps, self.agent_steps, self.prey_steps, self.predator_steps
            #returns 0 if predator moves into it
            if not self.predator.move(self.environment,self.pos):
                self.prey_steps.append(self.prey.pos)
                self.predator_steps.append(self.predator.pos)
                return 0, self.steps, self.agent_steps, self.prey_steps, self.predator_steps
        #returns -1 if timeout
        return -1, self.steps, self.agent_steps, self.prey_steps, self.predator_steps

def main():
    count = 0
    for _ in range(1):
        ag = Agent_1(verbose=True)
        k = ag.move()
        if k[0] == 1:
            count += 1 
        #print(k)
    print('---------------------------')
    print('Success count :' + str(count))
    print('Agent moves:')
    print(ag.agent_steps)
    print('Prey moves:')
    print(ag.prey_steps)
    print('Predator moves:')
    print(ag.predator_steps)
    print('pred, predy and agent last steps')
    print(ag.predator.pos)
    print(ag.prey.pos)
    print(ag.pos)

if __name__ == '__main__':
    main()
