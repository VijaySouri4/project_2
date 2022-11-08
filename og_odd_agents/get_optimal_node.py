#From the adjacent nodes list, iterate over all possible choices and find the most optimal node 
def get(adjacent_nodes,prey_dist_array,cur_prey_dist,pred_dist_array,cur_pred_dist):
            optimal_adjacent_node = adjacent_nodes[0]# Optimal node index
            optimal_prey_distance = prey_dist_array[0]# Distance to prey from the optimal node
            optimal_pred_distance = pred_dist_array[0]# Distance to predator from the optimal node
            cycle_flag = 0 # A flag that indicates if a higher priority choice is already triggered
            for k,i in enumerate(adjacent_nodes):
                #Iterate over the list of adjacent nodes
                if prey_dist_array[k] < cur_prey_dist and pred_dist_array[k] > cur_pred_dist:
                    # Inside each condition if there are multiple nodes that satisfied the condition, again pick the best based on the same priority
                    if prey_dist_array[k] < optimal_prey_distance and pred_dist_array[k] > optimal_pred_distance:
                        optimal_adjacent_node = i
                        optimal_prey_distance = prey_dist_array[k]
                        optimal_pred_distance = pred_dist_array[k]
                        cycle_flag += 1 # Update the cycle_flag variable to indicate that a higher priority condition has already been satisfied by the optimal_adjacent_node
                    elif prey_dist_array[k] < optimal_prey_distance and not pred_dist_array[k] < optimal_pred_distance:
                        optimal_adjacent_node = i
                        optimal_prey_distance = prey_dist_array[k]
                        optimal_pred_distance = pred_dist_array[k]
                        cycle_flag += 1
                    elif not prey_dist_array[k] > optimal_prey_distance and pred_dist_array[k] > optimal_pred_distance:
                        optimal_adjacent_node = i
                        optimal_prey_distance = prey_dist_array[k]
                        optimal_pred_distance = pred_dist_array[k]
                        cycle_flag += 1
                    elif not prey_dist_array[k] > optimal_prey_distance and not pred_dist_array[k] < optimal_pred_distance:
                        optimal_adjacent_node = i
                        optimal_prey_distance = prey_dist_array[k]
                        optimal_pred_distance = pred_dist_array[k]
                        cycle_flag += 1
                    elif pred_dist_array[k] > optimal_pred_distance:
                        optimal_adjacent_node = i
                        optimal_prey_distance = prey_dist_array[k]
                        optimal_pred_distance = pred_dist_array[k]
                        cycle_flag += 1
                    elif not pred_dist_array[k] < optimal_pred_distance:
                        optimal_adjacent_node = i
                        optimal_prey_distance = prey_dist_array[k]
                        optimal_pred_distance = pred_dist_array[k]
                        cycle_flag += 1

                elif prey_dist_array[k] < cur_prey_dist and pred_dist_array[k] >= cur_pred_dist:
                    if prey_dist_array[k] < optimal_prey_distance and pred_dist_array[k] > optimal_pred_distance and not cycle_flag > 0: # if the cycle_flag is greater than 0, it indicates that the above condition has already been accepted, so an optimal_adjacent_node already exists
                        optimal_adjacent_node = i
                        optimal_prey_distance = prey_dist_array[k]
                        optimal_pred_distance = pred_dist_array[k]
                        cycle_flag += 1 # Update cycle flag to indicate that a node with higher priority has been selected 
                    elif prey_dist_array[k] < optimal_prey_distance and not pred_dist_array[k] < optimal_pred_distance and not cycle_flag > 0:
                        optimal_adjacent_node = i
                        optimal_prey_distance = prey_dist_array[k]
                        optimal_pred_distance = pred_dist_array[k]
                        cycle_flag += 1
                    elif not prey_dist_array[k] > optimal_prey_distance and pred_dist_array[k] > optimal_pred_distance and not cycle_flag > 0:
                        optimal_adjacent_node = i
                        optimal_prey_distance = prey_dist_array[k]
                        optimal_pred_distance = pred_dist_array[k]
                        cycle_flag += 1
                    elif not prey_dist_array[k] > optimal_prey_distance and not pred_dist_array[k] < optimal_pred_distance and not cycle_flag > 0:
                        optimal_adjacent_node = i
                        optimal_prey_distance = prey_dist_array[k]
                        optimal_pred_distance = pred_dist_array[k]
                        cycle_flag += 1
                    elif pred_dist_array[k] > optimal_pred_distance and not cycle_flag > 0:
                        optimal_adjacent_node = i
                        cycle_flag += 1
                        optimal_prey_distance = prey_dist_array[k]
                        optimal_pred_distance = pred_dist_array[k]
                        cycle_flag += 1
                    elif not pred_dist_array[k] < optimal_pred_distance and not cycle_flag > 0:
                        optimal_adjacent_node = i
                        cycle_flag += 1
                        optimal_prey_distance = prey_dist_array[k]
                        optimal_pred_distance = pred_dist_array[k]
                        cycle_flag += 1

                elif not prey_dist_array[k] > cur_prey_dist and pred_dist_array[k] > cur_pred_dist:
                    if prey_dist_array[k] < optimal_prey_distance and pred_dist_array[k] > optimal_pred_distance and not cycle_flag > 0:
                        optimal_adjacent_node = i
                        optimal_prey_distance = prey_dist_array[k]
                        optimal_pred_distance = pred_dist_array[k]
                        cycle_flag += 1
                    elif prey_dist_array[k] < optimal_prey_distance and not pred_dist_array[k] < optimal_pred_distance and not cycle_flag > 0:
                        optimal_adjacent_node = i
                        optimal_prey_distance = prey_dist_array[k]
                        optimal_pred_distance = pred_dist_array[k]
                        cycle_flag += 1
                    elif not prey_dist_array[k] > optimal_prey_distance and pred_dist_array[k] > optimal_pred_distance and not cycle_flag > 0:
                        optimal_adjacent_node = i
                        optimal_prey_distance = prey_dist_array[k]
                        optimal_pred_distance = pred_dist_array[k]
                        cycle_flag += 1
                    elif not prey_dist_array[k] > optimal_prey_distance and not pred_dist_array[k] < optimal_pred_distance and not cycle_flag > 0:
                        optimal_adjacent_node = i
                        optimal_prey_distance = prey_dist_array[k]
                        optimal_pred_distance = pred_dist_array[k]
                        cycle_flag += 1
                    elif pred_dist_array[k] > optimal_pred_distance and not cycle_flag > 0:
                        optimal_adjacent_node = i
                        optimal_prey_distance = prey_dist_array[k]
                        optimal_pred_distance = pred_dist_array[k]
                        cycle_flag += 1
                    elif not pred_dist_array[k] < optimal_pred_distance and not cycle_flag > 0:
                        optimal_adjacent_node = i
                        optimal_prey_distance = prey_dist_array[k]
                        optimal_pred_distance = pred_dist_array[k]
                        cycle_flag += 1

                elif not prey_dist_array[k] > cur_prey_dist and not pred_dist_array[k] < cur_pred_dist:
                    if prey_dist_array[k] < optimal_prey_distance and pred_dist_array[k] > optimal_pred_distance and not cycle_flag > 0:
                        optimal_adjacent_node = i
                        optimal_prey_distance = prey_dist_array[k]
                        optimal_pred_distance = pred_dist_array[k]
                    elif prey_dist_array[k] < optimal_prey_distance and not pred_dist_array[k] < optimal_pred_distance and not cycle_flag > 0:
                        optimal_adjacent_node = i
                        optimal_prey_distance = prey_dist_array[k]
                        optimal_pred_distance = pred_dist_array[k]
                    elif not prey_dist_array[k] > optimal_prey_distance and pred_dist_array[k] > optimal_pred_distance and not cycle_flag > 0:
                        optimal_adjacent_node = i
                    elif not prey_dist_array[k] > optimal_prey_distance and not pred_dist_array[k] < optimal_pred_distance and not cycle_flag > 0:
                        optimal_adjacent_node = i
                        optimal_prey_distance = prey_dist_array[k]
                        optimal_pred_distance = pred_dist_array[k]
                        cycle_flag += 1
                    elif pred_dist_array[k] > optimal_pred_distance and not cycle_flag > 0:
                        optimal_adjacent_node = i
                        optimal_prey_distance = prey_dist_array[k]
                        optimal_pred_distance = pred_dist_array[k]
                        cycle_flag += 1
                    elif not pred_dist_array[k] < optimal_pred_distance and not cycle_flag > 0:
                        optimal_adjacent_node = i
                        optimal_prey_distance = prey_dist_array[k]
                        optimal_pred_distance = pred_dist_array[k]
                        cycle_flag += 1

                elif pred_dist_array[k] > cur_pred_dist:
                    if prey_dist_array[k] < optimal_prey_distance and pred_dist_array[k] > optimal_pred_distance and not cycle_flag > 0:
                        optimal_adjacent_node = i
                        optimal_prey_distance = prey_dist_array[k]
                        optimal_pred_distance = pred_dist_array[k]
                    elif prey_dist_array[k] < optimal_prey_distance and not pred_dist_array[k] < optimal_pred_distance and not cycle_flag > 0:
                        optimal_adjacent_node = i
                        optimal_prey_distance = prey_dist_array[k]
                        optimal_pred_distance = pred_dist_array[k]
                    elif not prey_dist_array[k] > optimal_prey_distance and pred_dist_array[k] > optimal_pred_distance and not cycle_flag > 0:
                        optimal_adjacent_node = i
                        optimal_prey_distance = prey_dist_array[k]
                        optimal_pred_distance = pred_dist_array[k]
                    elif not prey_dist_array[k] > optimal_prey_distance and not pred_dist_array[k] < optimal_pred_distance and not cycle_flag > 0:
                        optimal_adjacent_node = i
                        optimal_prey_distance = prey_dist_array[k]
                        optimal_pred_distance = pred_dist_array[k]
                        cycle_flag += 1
                    elif pred_dist_array[k] > optimal_pred_distance and not cycle_flag > 0:
                        optimal_adjacent_node = i
                        optimal_prey_distance = prey_dist_array[k]
                        optimal_pred_distance = pred_dist_array[k]
                        cycle_flag += 1
                    elif not pred_dist_array[k] < optimal_pred_distance and not cycle_flag > 0:
                        optimal_adjacent_node = i
                        optimal_prey_distance = prey_dist_array[k]
                        optimal_pred_distance = pred_dist_array[k]
                        cycle_flag += 1

                elif not pred_dist_array[k] < cur_pred_dist:
                    if prey_dist_array[k] < optimal_prey_distance and pred_dist_array[k] > optimal_pred_distance and not cycle_flag > 0:
                        optimal_adjacent_node = i
                        optimal_prey_distance = prey_dist_array[k]
                        optimal_pred_distance = pred_dist_array[k]
                    elif prey_dist_array[k] < optimal_prey_distance and not pred_dist_array[k] < optimal_pred_distance and not cycle_flag > 0:
                        optimal_adjacent_node = i
                        optimal_prey_distance = prey_dist_array[k]
                        optimal_pred_distance = pred_dist_array[k]
                    elif not prey_dist_array[k] > optimal_prey_distance and pred_dist_array[k] > optimal_pred_distance and not cycle_flag > 0:
                        optimal_adjacent_node = i
                        optimal_prey_distance = prey_dist_array[k]
                        optimal_pred_distance = pred_dist_array[k]
                    elif not prey_dist_array[k] > optimal_prey_distance and not pred_dist_array[k] < optimal_pred_distance and not cycle_flag > 0:
                        optimal_adjacent_node = i
                        optimal_prey_distance = prey_dist_array[k]
                        optimal_pred_distance = pred_dist_array[k]
                        cycle_flag += 1
                    elif pred_dist_array[k] > optimal_pred_distance and not cycle_flag > 0:
                        optimal_adjacent_node = i
                        optimal_prey_distance = prey_dist_array[k]
                        optimal_pred_distance = pred_dist_array[k]
                        cycle_flag += 1
                    elif not pred_dist_array[k] < optimal_pred_distance and not cycle_flag > 0:
                        optimal_adjacent_node = i
                        optimal_prey_distance = prey_dist_array[k]
                        optimal_pred_distance = pred_dist_array[k]
                        cycle_flag += 1
            
            result_index = optimal_adjacent_node

            return result_index