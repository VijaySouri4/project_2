import environment
import pygame
import predator
import prey
import random
import math
import networkx as nx
import copy
import agent_1 as ag1
import agent_3 as ag3
import agent_2 as ag2
import agent_4 as ag4
import agent_5 as ag5
import agent_6 as ag6
import agent_7 as ag7
import agent_8 as ag8
import PIL
import os

class Animation:
    def __init__(self,env = None,prey_moves = None,pred_moves = None,agent_moves = None, actual_prey_moves = None, actual_predator_moves = None) -> None:
        self.env = env
        self.prey_moves = prey_moves
        self.pred_moves = pred_moves
        self.agent_moves = agent_moves
        self.actual_prey_moves = actual_prey_moves
        self.actual_pred_moves = actual_predator_moves

        self.display_width = 1080
        self.display_height = 720
        self.radius = self.display_width/100 #radius of node
        self.screen = pygame.display.set_mode((self.display_width,self.display_height))
        self.clock = pygame.time.Clock() #Pygame clock
        self.speed = 1.5 #FPS

        ## Colors and their definitions
        self.grey = (100, 100, 100)  # Normal node without prey, predator or agent
        self.white = (255, 255, 255)  # Edge color
        self.yellow = (200, 200, 0)  # Agent Node
        self.something = (111, 111, 111)
        self.red = (200,0,0) # Predator Node
        self.black = (0, 0, 0)  # Prey Node
        self.orange = (255,215,0) #outerline for predator
        self.green = (0, 255, 127) # Success
        self.violet = (51, 0, 102) # Alt agent
        self.blue = (240,248,255) #timeout
        self.cream = (255, 253, 208) #alt to grey

        ## Initialise pygame constants

        pygame.init()

        self.screen.fill((255,255,255))

        self.x_pos = []
        self.y_pos = []

        '''
        this implementation of node cordinates is not very bespoke
        Needs a lot of adaptation through pygame to make it work
        G = nx.Graph()
        for i in range(self.env.number_of_nodes):
            G.add_node(i)
        pos = nx.circular_layout(G, scale=800, center=[500,500], dim=2)
        circular_cords = pos.values()
        '''
        w, h = pygame.display.get_surface().get_size()
        # Assigning coordinates to each of the nodes
        for i in range(self.env.number_of_nodes):
            con = 360/self.env.number_of_nodes * i
            self.x_pos.append((h/2.2*math.cos(math.radians(con)))+w/2) # 950 is the x offsett for my framework laptop screen
            self.y_pos.append((h/2.2*math.sin(math.radians(con)))+h/2) # 700 is the y axis offset for my framework laptop screen

        self.animation()

    def edge_normaliser(self,n1,n2):
        # Avoiding duplicate edges in the edge set
        return tuple(sorted((n1,n2)))

    def draw_edges(self):
        #create a set that contains all the edges in the 50 nodes graph and plot it with pygame 
        nodes = self.env.lis
        edges = {}
        for i in nodes:
            adj_list = [i.left_node_index,i.right_node_index,i.other_node_index]
            if i.other_node_index == i.index:
                adj_list.pop()
            for j in adj_list:
                temp = i.index
                edge = self.edge_normaliser(temp,j)
                if edge not in edges:
                    edges[edge] = [(i.index,j), self.grey]

        for n1,n2 in edges:
            #Here n1 is the index of one node and n2 is the index of the other node
            #Here we draw a line between these two nodes
            #The cordinates of each node of index i is present in self.x_pos[i] and self.y_pos[i]
            pygame.draw.line(self.screen,self.black,(self.x_pos[n1],self.y_pos[n1]),(self.x_pos[n2],self.y_pos[n2]),2)
            #print("The cords for node "+str(n1)+" are :{:.2f}  {:.2f}".format(self.x_pos[n1],self.y_pos[n1]))

        


    def create_circles(self):
        
        #[pygame.draw.circle(screen, (255,255,200),tuple((x[0]*1000,x[1]*1000)), self.radius) for x in circular_cords]
        for w,i in enumerate(zip(self.x_pos,self.y_pos)):
            if w == self.actual_prey_pos and w == self.agent_pos: ## Denotes success
                pygame.draw.circle(self.screen,self.success, i, self.radius) # default is filled circle
                pygame.draw.circle(self.screen, self.success, i, self.radius-4)
            elif w == self.agent_pos and w == self.actual_pred_pos:
                pygame.draw.circle(self.screen,self.failure, i, self.radius) # default is filled circle
                pygame.draw.circle(self.screen, self.failure, i, self.radius-4)
            elif w == self.agent_pos: # Denotes position of agent
                pygame.draw.circle(self.screen,self.agent_color, i, self.radius) # default is filled circle
                pygame.draw.circle(self.screen, self.agent_color, i, self.radius-4)
            elif w == self.actual_prey_pos: # Denotes position of actual_prey
                pygame.draw.circle(self.screen,self.actual_prey_color, i, self.radius) # default is filled circle
                pygame.draw.circle(self.screen, self.actual_prey_color, i, self.radius-4)
            elif w == self.actual_pred_pos: # Denotes position of actual_prey
                pygame.draw.circle(self.screen,self.actual_pred_color, i, self.radius) # default is filled circle
                pygame.draw.circle(self.screen, self.actual_pred_color, i, self.radius-4)
            elif w == self.pred_pos: # Denotes position of believed predator
                pygame.draw.circle(self.screen,self.actual_pred_color_outer, i, self.radius) # default is filled circle
                pygame.draw.circle(self.screen, self.pred_color, i, self.radius-4)
            elif w == self.prey_pos: # Denotes position of believed Prey 
                pygame.draw.circle(self.screen,self.actual_pred_color_outer, i, self.radius) # default is filled circle
                pygame.draw.circle(self.screen, self.prey_color, i, self.radius-4)
            else: # Denotes non actor containing node
                pygame.draw.circle(self.screen,self.non_actor_color, i, self.radius) # default is filled circle
                pygame.draw.circle(self.screen, self.non_actor_color, i, self.radius-4)

        #pygame.draw.circle(screen, (255,255,200), (circular_cords[0][0]*1000,circular_cords[0][1]*1000),self.radius)
        '''
        for x,y in zip(x_pos,y_pos):
            pygame.draw.circle(screen, # draw need buffer
            (255,255,200), # color of circle
            (x,y), self.radius) # default is filled circle
            pygame.draw.circle(screen, 
            (0,150,150), (x,y), self.radius-4)
        '''
    #def create_graph(self):


    def legend(self):
        '''self.success = self.green
        self.agent_color = self.yellow
        self.prey_color = self.violet
        self.pred_color = self.red
        self.actual_pred_color = self.red
        self.actual_pred_color_outer = self.orange
        self.actual_prey_color = self.violet
        self.actual_prey_color_outer = self.green'''
        if self.agent_pos == self.actual_prey_pos and self.agent_pos == self.actual_pred_pos:
            font = pygame.font.Font('freesansbold.ttf', 32)
            text = font.render('Unique Situation', True, self.green, self.black)
            textRect = text.get_rect()
            textRect.center = (self.display_width // 2, (self.display_height // 2) - 40 )
            self.screen.blit(text, textRect)
        elif self.agent_pos == self.actual_prey_pos:
            font = pygame.font.Font('freesansbold.ttf', 32)
            text = font.render('Simulation Ended, Caught prey', True, self.green, self.black)
            textRect = text.get_rect()
            textRect.center = (self.display_width // 2, (self.display_height // 2) - 40 )
            self.screen.blit(text, textRect)
        elif self.agent_pos == self.actual_pred_pos:
            font = pygame.font.Font('freesansbold.ttf', 32)
            text = font.render('Simulation Ended, Agent Died', True, self.green, self.black)
            textRect = text.get_rect()
            textRect.center = (self.display_width // 2, (self.display_height // 2) - 40 )
            self.screen.blit(text, textRect)
        elif self.agent_pos != self.prey_pos and self.agent_pos != self.pred_pos:

            font = pygame.font.Font('freesansbold.ttf', 32)
            text = font.render('Yellow Denotes Agent', True, self.yellow, self.black)
            textRect = text.get_rect()
            textRect.center = (self.display_width // 2, self.display_height // 2 )
            self.screen.blit(text, textRect)
            text = font.render('Violet Denotes Prey', True, self.violet, self.cream)
            textRect = text.get_rect()
            textRect.center = (self.display_width // 2, (self.display_height // 2) + 40 )
            self.screen.blit(text, textRect)
            text = font.render('Red Denotes Predator', True, self.red, self.black)
            textRect = text.get_rect()
            textRect.center = (self.display_width // 2, (self.display_height // 2) + 80 )
            self.screen.blit(text, textRect)
            text = font.render('Green Denotes Catch', True, self.green, self.black)
            textRect = text.get_rect()
            textRect.center = (self.display_width // 2, (self.display_height // 2) + 120)
            self.screen.blit(text, textRect)
            text = font.render('Green Denotes Catch', True, self.green, self.black)
            textRect = text.get_rect()
            textRect.center = (self.display_width // 2, (self.display_height // 2) + 120)
            self.screen.blit(text, textRect)
            text = font.render('Hollow Denotes Belief', True, self.orange, self.black)
            textRect = text.get_rect()
            textRect.center = (self.display_width // 2, (self.display_height // 2) + 120)
            self.screen.blit(text, textRect)


    def animation(self):

        self.success = self.green
        self.agent_color = self.yellow
        self.prey_color = self.violet
        self.pred_color = self.red
        self.actual_pred_color = self.red
        self.actual_pred_color_outer = self.orange
        self.actual_prey_color = self.violet
        self.actual_prey_color_outer = self.green
        self.timeout = self.blue
        self.failure = self.black
        self.non_actor_color = self.cream

        moves_list = [self.agent_moves,self.prey_moves, self.pred_moves, self.actual_prey_moves, self.actual_pred_moves]
        len_list = [len(self.agent_moves),len(self.pred_moves),len(self.prey_moves), len(self.actual_prey_moves), len(self.actual_pred_moves)]

        print('Moves are as follows:'+str(moves_list))
        print('The lengths of these lists are as follows:'+str(len_list))
        if len(self.agent_moves) == max(len_list):
            pass
        else:
            for i in moves_list:
                if len(i) != max(len_list):
                    i.append(i[len(i)-1])

        self.agent_moves = moves_list[0]
        self.prey_moves = moves_list[1]
        self.pred_moves = moves_list[2]
        

        for i,j,k,l,m in zip(self.agent_moves,self.prey_moves,self.pred_moves,self.actual_prey_moves,self.actual_pred_moves):
            print(i, j, k, l, m)
            self.agent_pos = i #yellow color
            self.prey_pos = j #black color
            self.pred_pos = k #red color
            self.actual_prey_pos = l
            self.actual_pred_pos = m
            
            self.update() # copy screen to display

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
        
        pygame.quit()

    def draw_graph(self):
        self.draw_edges()
        self.create_circles()
        self.legend()


    def update(self):
        self.draw_graph()
        pygame.display.set_caption('Simulation')
        pygame.display.update()
        self.clock.tick(self.speed)

def main():
    input_environment = environment.Env(50)
    input_predator = predator.Predator()
    input_prey = prey.Prey() 
    input_pos = random.choice(range(0,49))

    #make sure agent doesnt start in occupied node
    while input_prey.pos == input_pos or input_predator.pos == input_pos:
        input_pos = random.choice(range(0,49))
    
    '''
    agent_1 = ag3.Agent_3(copy.deepcopy(input_predator), copy.deepcopy(input_prey), copy.deepcopy(env), input_pos)
    result_1, steps, agent_steps, prey_steps, predator_steps, actual_prey_steps, actual_predator_steps = agent_1.move()
    test = Animation(env,prey_steps, predator_steps, agent_steps, actual_prey_steps, actual_predator_steps)
    '''

    agent = ag4.Agent_4(copy.deepcopy(input_predator), copy.deepcopy(input_prey), copy.deepcopy(input_environment), input_pos)
    k = agent.move()
    prey_steps = agent.prey_steps
    predator_steps = agent.predator_steps
    agent_steps = agent.agent_steps
    actual_prey_steps = agent.actual_prey_steps
    actual_predator_steps = agent.actual_predator_steps

    test = Animation(input_environment,prey_steps, predator_steps, agent_steps, actual_prey_steps, actual_predator_steps)
if __name__ == '__main__':
    main() 