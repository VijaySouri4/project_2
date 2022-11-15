import environment
import pygame
import predator
import prey
import random
import math
import networkx as nx
import copy
import agent_1 as ag1
import agent_2 as ag2
import agent_3 as ag3
import agent_4 as ag4
import agent_5 as ag5
import agent_6 as ag6
import agent_7 as ag7
import agent_7_defect as ag7d
import agent_7_defect_updated as ag7du
import agent_8 as ag8
import agent_8_defect as ag8d
import agent_8_defect_updated as ag8du

import animation as an


def main():

    input_environment = environment.Env(50)
    input_predator = predator.Predator()
    input_prey = prey.Prey() 
    input_pos = random.choice(range(0,49))

    #make sure agent doesnt start in occupied node
    while input_prey.pos == input_pos or input_predator.pos == input_pos:
        input_pos = random.choice(range(0,49))
        
    agent = ag1.Agent_1(copy.deepcopy(input_predator), copy.deepcopy(input_prey), copy.deepcopy(input_environment), input_pos)
    k = agent.move()
    prey_steps = agent.prey_steps
    predator_steps = agent.predator_steps
    agent_steps = agent.agent_steps
    actual_prey_steps = agent.actual_prey_steps
    actual_predator_steps = agent.actual_predator_steps
    test = an.Animation(input_environment,prey_steps, predator_steps, agent_steps, actual_prey_steps, actual_predator_steps)

    agent = ag2.Agent_2(copy.deepcopy(input_predator), copy.deepcopy(input_prey), copy.deepcopy(input_environment), input_pos)
    k = agent.move()
    prey_steps = agent.prey_steps
    predator_steps = agent.predator_steps
    agent_steps = agent.agent_steps
    actual_prey_steps = agent.actual_prey_steps
    actual_predator_steps = agent.actual_predator_steps
    test = an.Animation(input_environment,prey_steps, predator_steps, agent_steps, actual_prey_steps, actual_predator_steps)

    agent = ag3.Agent_3(copy.deepcopy(input_predator), copy.deepcopy(input_prey), copy.deepcopy(input_environment), input_pos)
    k = agent.move()
    prey_steps = agent.prey_steps
    predator_steps = agent.predator_steps
    agent_steps = agent.agent_steps
    actual_prey_steps = agent.actual_prey_steps
    actual_predator_steps = agent.actual_predator_steps
    test = an.Animation(input_environment,prey_steps, predator_steps, agent_steps, actual_prey_steps, actual_predator_steps)

    agent = ag4.Agent_4(copy.deepcopy(input_predator), copy.deepcopy(input_prey), copy.deepcopy(input_environment), input_pos)
    k = agent.move()
    prey_steps = agent.prey_steps
    predator_steps = agent.predator_steps
    agent_steps = agent.agent_steps
    actual_prey_steps = agent.actual_prey_steps
    actual_predator_steps = agent.actual_predator_steps
    test = an.Animation(input_environment,prey_steps, predator_steps, agent_steps, actual_prey_steps, actual_predator_steps)

    agent = ag5.Agent_5(copy.deepcopy(input_predator), copy.deepcopy(input_prey), copy.deepcopy(input_environment), input_pos)
    k = agent.move()
    prey_steps = agent.prey_steps
    predator_steps = agent.predator_steps
    agent_steps = agent.agent_steps
    actual_prey_steps = agent.actual_prey_steps
    actual_predator_steps = agent.actual_predator_steps
    test = an.Animation(input_environment,prey_steps, predator_steps, agent_steps, actual_prey_steps, actual_predator_steps)

    agent = ag6.Agent_6(copy.deepcopy(input_predator), copy.deepcopy(input_prey), copy.deepcopy(input_environment), input_pos)
    k = agent.move()
    prey_steps = agent.prey_steps
    predator_steps = agent.predator_steps
    agent_steps = agent.agent_steps
    actual_prey_steps = agent.actual_prey_steps
    actual_predator_steps = agent.actual_predator_steps
    test = an.Animation(input_environment,prey_steps, predator_steps, agent_steps, actual_prey_steps, actual_predator_steps)

    agent = ag7.Agent_7(copy.deepcopy(input_predator), copy.deepcopy(input_prey), copy.deepcopy(input_environment), input_pos)
    k = agent.move()
    prey_steps = agent.prey_steps
    predator_steps = agent.predator_steps
    agent_steps = agent.agent_steps
    actual_prey_steps = agent.actual_prey_steps
    actual_predator_steps = agent.actual_predator_steps
    test = an.Animation(input_environment,prey_steps, predator_steps, agent_steps, actual_prey_steps, actual_predator_steps)

    agent = ag8.Agent_8(copy.deepcopy(input_predator), copy.deepcopy(input_prey), copy.deepcopy(input_environment), input_pos)
    k = agent.move()
    prey_steps = agent.prey_steps
    predator_steps = agent.predator_steps
    agent_steps = agent.agent_steps
    actual_prey_steps = agent.actual_prey_steps
    actual_predator_steps = agent.actual_predator_steps
    test = an.Animation(input_environment,prey_steps, predator_steps, agent_steps, actual_prey_steps, actual_predator_steps)






if __name__ == '__main__':
    main()