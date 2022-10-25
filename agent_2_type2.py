from operator import indexOf
import random
import predator
import prey
import environment
import math

class Agent_2_2:

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

        self.verbose = verbose
        self.steps = 0

        #make sure agent doesnt start in occupied node
        while self.prey.pos == self.pos or self.predator.pos == self.pos:
            self.pos = random.choice(range(0,49))

    """Movement function for agent 1
    returns 1 if catches prey, 0 if dies, -1 if timeout"""

    def move(self):
        #runs for 100 steps else returns false
        while self.steps <= 200:
            self.steps += 1

            '''
            Make a cloud similar to the agent 2 in project 1. When the agent is less than three 
            steps away from the predator, then only prefer to move away from the predator, else 
            just move towards the prey.(Wait I dont think this will work, cause the predator will 
            keep chasing you)
            '''
            predator_pos = self.predator.pos
            prey_pos = self.prey.pos
            current_node = self.environment.lis[self.pos]
            shortest_paths = self.environment.shortest_paths

            #array of possible choices
            adjacent_nodes = [current_node.left_node_index,
            current_node.right_node_index,
            current_node.other_node_index]

            #gets distances to predator from each direction
            left_pred_dist = shortest_paths[current_node.left_node_index][predator_pos][0]
            right_pred_dist = shortest_paths[current_node.right_node_index][predator_pos][0]
            other_pred_dist = shortest_paths[current_node.other_node_index][predator_pos][0]
            cur_pred_dist = shortest_paths[self.pos][predator_pos][0]

            #puts distances from predator in array
            pred_dist_array = [left_pred_dist, right_pred_dist, other_pred_dist]

            if min(pred_dist_array) < 3: # if the predator is closer to the agent, just prioritise getting away
                count = 0 # count the number of times you are moving away
                maxi = max(pred_dist_array)
                next_node_index = pred_dist_array.index(maxi)
                if next_node_index == 0:
                    self.pos = current_node.left_node_index
                elif next_node_index == 1:
                    self.pos = current_node.right_node_index
                else:
                    self.pos = current_node.other_node_index
                if self.verbose:
                    self.status(predator_pos,prey_pos)
                if self.predator.pos == self.pos or not self.predator.move(self.environment,self.pos):
                    if self.verbose:
                        self.status(predator_pos,prey_pos)
                    return 0
                #returns 1 if moves into prey or prey moves into it
                if self.prey.pos == self.pos or not self.prey.move(self.environment,self.pos):
                    if self.verbose:
                        self.status(predator_pos,prey_pos)
                    return 1
            else:

                #gets distances to prey from each direction
                left_prey_dist = shortest_paths[current_node.left_node_index][prey_pos ][0]
                right_prey_dist = shortest_paths[current_node.right_node_index][prey_pos ][0]
                other_prey_dist = shortest_paths[current_node.other_node_index][prey_pos ][0]
                cur_prey_dist = shortest_paths[self.pos][prey_pos][0]

                #puts distances from prey in array
                prey_dist_array = [left_prey_dist, right_prey_dist, other_prey_dist]
                if self.verbose:
                    self.status(predator_pos,prey_pos)
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
                    if self.verbose:
                        self.status(predator_pos,prey_pos)
                    return 0
                #returns 1 if moves into prey or prey moves into it
                if self.prey.pos == self.pos or not self.prey.move(self.environment,self.pos):
                    if self.verbose:
                        self.status(predator_pos,prey_pos)
                    return 1

        #returns -1 if timeout
        if self.verbose:
            print('%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%')
            print('Timed out:')
            self.status(predator_pos,prey_pos)
        return -1
    
    def status(self,predator_pos,prey_pos):
        print('The current node is:'+str(self.pos))
        print('The predator node is:'+str(predator_pos))
        print('The prey node is:'+str(prey_pos))
        print('-----------------------------------------------------')



def main():
    count = 0
    for _ in range(50):
        ag = Agent_2_2(verbose=True)
        k = ag.move()
        if k == 1:
            count += 1 
        print(k)
    print('---------------------------')
    print('Success count :' + str(count))

if __name__ == '__main__':
    main()