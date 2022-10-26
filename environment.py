from ast import main
from copy import copy
from operator import index
from queue import Empty
import node
import matplotlib.pyplot as plt
import networkx as nx
import random
import math
import numpy as np

class Env:

    def __init__(self,number_of_nodes = 50) -> None:
        # Taking the number of nodes for initial simplicity
        self.number_of_nodes = number_of_nodes
        # call function to construct the graph
        self.construct()

    def construct(self):
        # main list that holds all the node objects
        self.lis = []
        # list that holds shortest paths for each node
        self.shortest_paths = []
        #may be I could implement shortest path as a dictionary 
        self.shortest_paths_dic = {}
        # set that contains all the edges with respect to the index of nodes
        edges_lis = set()
        # initialising the circular nodes
        for i in range(self.number_of_nodes):
            if i == 0:
                nd = node.Node(i,self.number_of_nodes - 1,i+1,degree=2)
                if (i+1,i) not in edges_lis:        #prevent duplicate edges
                    edges_lis.add((i,i+1))
                if ((self.number_of_nodes - 1), i) not in edges_lis:    #prevent duplicate edges
                    edges_lis.add((i,self.number_of_nodes - 1))
                self.lis.append(nd)
            elif i == self.number_of_nodes - 1: # lol sorry for the roundabout implementation 
                nd = node.Node(i,i-1,0,degree=2)
                if (0,i) not in edges_lis:  #prevent duplicate edges
                    edges_lis.add((i,0))
                if (i-1, i) not in edges_lis:
                    edges_lis.add((i,i-1))  #prevent duplicate edges
                self.lis.append(nd)
            else:
                nd = node.Node(i,i-1,i+1,degree=2)
                if (i+1, i) not in edges_lis:   #prevent duplicate edges
                    edges_lis.add((i,i+1))
                if (i-1, i) not in edges_lis:   #prevent duplicate edges
                    edges_lis.add((i,i-1))
                self.lis.append(nd)
        
        # Randomly create edges between graph nodes
        check_nodes= [x for x in range(0,50)]
        additional_edges = 0
        while check_nodes:
            #loop_iter = loop_iter - 1
            index = random.randint(0,len(check_nodes) - 1) # now it should run well everytime
            rand_node_1 = check_nodes[index]
            del check_nodes[index]
            # check if the selected node has a degree of 3, proceed if not
            temp_node = self.lis[rand_node_1] # This is breaking. Why? # lol, your range for generating random numbers is improper
            if temp_node.degree < 3:   
                
                
                # implement a function to get the five surrounding neighbor's indexes
                neighbors = self.get_five_neighbors(rand_node_1)
                if not neighbors:   #check if list is empty
                    continue
                choice = random.choices(neighbors,weights=None,k=1)
                
                temp_node.degree = temp_node.degree + 1

                    #not sure if needed anymore since I updated get_five_neightbors so only degree of < 3
                    #yup not needed anymore thanks Michael, you the best, like DJ khalid. # Damn sorry I get goofy when I write code
                selected_node = self.lis[choice[0]]
                
                #print(choice[0])

                # Now change the other node value for both the objects and increment the degree by one to both the nodes
                temp_node.other_node_index = choice[0]
                selected_node.other_node_index = temp_node.index

                selected_node.degree = selected_node.degree + 1

                self.lis[rand_node_1] = temp_node
                self.lis[choice[0]] = selected_node

                # add the edge into the edge set
                edges_lis.add((rand_node_1,choice[0]))
                additional_edges += 1
        
        #calls recursive bfs and stores results in 2D array
        self.generate_shortest_paths()

        """
        G = nx.Graph()
        #create circular position for graph
        for i in range(self.number_of_nodes):
            con = 360/self.number_of_nodes * i
            x_pos = (1*math.cos(math.radians(con)))
            y_pos = (1*math.sin(math.radians(con)))
            G.add_node(i,pos = (x_pos,y_pos))
        G.add_edges_from(edges_lis)
        nx.draw_networkx(G, nx.get_node_attributes(G,'pos'), node_size=80, alpha=0.75, font_size=8, font_weight=0.5)
        plt.show()"""
        #print(additional_edges)
        
        

    def get_five_neighbors(self,index):
        up_counter = 5
        temp_index = index
        output = []
        while up_counter > 0:
            up_counter = up_counter - 1
            if (temp_index + 1) >= self.number_of_nodes:
                original_temp_index = temp_index + 1
                temp_index = 0
                if self.lis[temp_index].degree < 3 and original_temp_index != index + 1: #prevent it from adding indexes with degree of 3 or node that is directly next to it
                    output.append(temp_index)
            else:
                temp_index = temp_index + 1
                if self.lis[temp_index].degree < 3 and temp_index != index + 1: #prevent it from adding indexes with degree of 3 or node that is directly next to it
                    #nice catch I did not think of this immediate node thing 
                    output.append(temp_index)
        up_counter = 5
        temp_index = index
        while up_counter > 0:
            up_counter = up_counter - 1
            if (temp_index - 1) < 0:
                original_temp_index = temp_index - 1
                temp_index = self.number_of_nodes - 1
                if self.lis[temp_index].degree < 3 and original_temp_index != index - 1: #prevent it from adding indexes with degree of 3 or node that is directly next to it
                    output.append(temp_index)
            else:
                temp_index = temp_index - 1
                if self.lis[temp_index].degree < 3 and temp_index != index - 1: #prevent it from adding indexes with degree of 3 or node that is directly next to it
                    output.append(temp_index)

        return output

    """Runs recursive BFS for each node and stores it in 2D array"""
    
    def generate_shortest_paths(self):
        for node in self.lis:
            self.shortest_paths.append(self.node_bfs(node))
        return


    """Recursive BFS algo, returns array of shortest paths from node to i, where array [i] =
    (distance , path), the path for node to i is [node index, ... i - 1]"""

    def node_bfs(self, node, depth = 0, visited = None, prev_list = []):
        index = node.index
        #depth gives cost of reaching a node

        # visited is a list of tuples that contains cost of reaching from the current node in the 0th index and a list of nodes that make up the path 
        
        if visited is None:   #base case for first call
                  
            visited = [(math.inf,[])] * self.number_of_nodes
            #print(visited)
            visited[index] = (0, [])
        
        right = node.right_node_index
        left = node.left_node_index
        other = node.other_node_index
        if visited[right][0] >= depth + 1:  #run recursive bfs on right node
            if visited[right][0] == depth + 1:       
                new_list = prev_list[:]
                new_list.append(right) 
                current_list = visited[right][1][:]
                current_list.append(new_list)
            else:
                new_list = prev_list[:]
                new_list.append(right)
                current_list = [new_list]
            visited[right] = (depth + 1, current_list)
            self.node_bfs(self.lis[right], depth+1, visited, new_list)
        

        if visited[left][0] >= depth + 1:  #run recursive bfs on left node
            if visited[left][0] == depth + 1:    
                new_list = prev_list[:]
                new_list.append(left) 
                current_list = visited[left][1][:]
                current_list.append(new_list)
            else:
                new_list = prev_list[:]
                new_list.append(left)
                current_list = [new_list]
                visited[left] = (depth + 1, current_list)
            self.node_bfs(self.lis[left], depth+1, visited, new_list)

        if other != index and visited[other][0] >= depth + 1:  #run recursive bfs on other node if exists
            if visited[other][0] == depth + 1:    
                new_list = prev_list[:]
                new_list.append(other)   
                current_list = visited[other][1][:]  
                current_list.append(new_list)
            else:
                new_list = prev_list[:]
                new_list.append(other)
                current_list = [new_list]
            visited[other] = (depth + 1, current_list)
            self.node_bfs(self.lis[other], depth+1, visited, new_list)

        return visited



def main():
    test = Env(50)

if __name__ == '__main__':
    main()

