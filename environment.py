from ast import main
import node
import matplotlib.pyplot as plt
import networkx as nx
import random

class Env:

    def __init__(self,number_of_nodes = 50) -> None:
        # Taking the number of nodes for initial simplicity
        self.number_of_nodes = number_of_nodes
        # call function to construct the graph
        self.construct()

    def construct(self):
        # main list that holds all the node objects
        self.lis = []
        # set that contains all the edges with respect to the index of nodes
        edges_lis = set()
        # initialising the circular nodes
        for i in range(self.number_of_nodes):
            if i == 0:
                nd = node.Node(i,self.number_of_nodes - 1,i+1,degree=2)
                edges_lis.add((i,i+1))
                edges_lis.add((i,self.number_of_nodes - 1))
                self.lis.append(nd)
            elif i == self.number_of_nodes - 1: # lol sorry for the roundabout implementation 
                nd = node.Node(i,i-1,0,degree=2)
                edges_lis.add((i,0))
                edges_lis.add((i,i-1))
                self.lis.append(nd)
            else:
                nd = node.Node(i,i-1,i+1,degree=2)
                edges_lis.add((i,i+1))
                edges_lis.add((i,i-1))
                self.lis.append(nd)
        
        # Randomly create edges between graph nodes
        loop_iter = int(self.number_of_nodes / 2)
        while loop_iter > 0:
            #loop_iter = loop_iter - 1
            rand_node_1 = random.randint(0,self.number_of_nodes)
            # check if the selected node has a degree of 3, proceed if not
            temp_node = self.lis[rand_node_1]
            if temp_node.degree < 3:   
                loop_iter = loop_iter - 1
                temp_node.degree = temp_node.degree + 1
                
                # implement a function to get the five surrounding neighbor's indexes
                neighbors = self.get_five_neighbors(rand_node_1)
                choice = random.choices(neighbors,weights=None,k=1)

                try:
                    selected_node = self.lis[choice[0]]
                except:
                    continue
                if selected_node.degree < 3:
                    print(choice[0])

                    # Now change the other node value for both the objects and increment the degree by one to both the nodes
                    temp_node.other_node_index = choice[0]
                    selected_node.other_node_index = temp_node.index

                    selected_node.degree = selected_node.degree + 1

                    self.lis[rand_node_1] = temp_node
                    self.lis[choice[0]] = selected_node

                    # add the edge into the edge set
                    edges_lis.add((rand_node_1,choice[0]))



        G = nx.Graph()
        G.add_edges_from(edges_lis)
        nx.draw_networkx(G)
        plt.show()

    def get_five_neighbors(self,index):
        up_counter = 5
        temp_index = index
        output = []
        while up_counter > 0:
            up_counter = up_counter - 1
            if (temp_index + 1) > self.number_of_nodes:
                temp_index = 0
                output.append(temp_index)
            else:
                temp_index = temp_index + 1
                output.append(temp_index)
        up_counter = 5
        temp_index = index
        while up_counter > 0:
            up_counter = up_counter - 1
            if (temp_index - 1) < 0:
                temp_index = self.number_of_nodes
                output.append(temp_index)
            else:
                temp_index = temp_index - 1
                output.append(temp_index)

        return output




def main():
    test = Env(20)

if __name__ == '__main__':
    main()

