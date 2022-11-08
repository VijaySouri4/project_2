import numpy as np
class Node:

    def __init__(self,index,left_node_index = np.nan,right_node_index = np.nan,other_node_index = np.nan,degree = 1) -> None:
        self.index = index
        self.left_node_index = left_node_index
        self.right_node_index = right_node_index
        if other_node_index is np.nan:
           self.other_node_index = index
        else:
            self.other_node_index = other_node_index 
        self.degree = degree