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
import agent_5 as ag5
import agent_7 as ag7
import animation


def main():

    input_environment = environment.Env(50)
    input_predator = predator.Predator()
    input_prey = prey.Prey() 
    input_pos = random.choice(range(0,49))

    #make sure agent doesnt start in occupied node
    while input_prey.pos == input_pos or input_predator.pos == input_pos:
        input_pos = random.choice(range(0,49))

    agent_1 = ag1.Agent_1(copy.deepcopy(input_predator), copy.deepcopy(input_prey), copy.deepcopy(input_environment), input_pos)
    _, _, agent_steps, prey_steps, predator_steps, actual_prey_steps, actual_predator_steps = agent_1.move()
    print('Agent 1')
    print('------------------------------------------')
    print('Agent moves:')
    print(agent_steps)
    print('Prey moves:')
    print(prey_steps)
    print('Predator moves:')
    print(predator_steps)
    test = animation.Animation(input_environment,prey_steps, predator_steps, agent_steps, actual_prey_steps, actual_predator_steps)


    agent_3 = ag3.Agent_3(copy.deepcopy(input_predator), copy.deepcopy(input_prey), copy.deepcopy(input_environment), input_pos)
    _, _, agent_steps, prey_steps, predator_steps, actual_prey_steps, actual_predator_steps= agent_3.move()
    test = animation.Animation(input_environment,prey_steps, predator_steps, agent_steps, actual_prey_steps, actual_predator_steps)

    print('------------------------------------------')
    print('Agent 3')
    print('Agent moves:')
    print(agent_steps)
    print('Prey moves:')
    print(prey_steps)
    print('Predator moves:')
    print(predator_steps)


    agent_5 = ag5.Agent_5(copy.deepcopy(input_predator), copy.deepcopy(input_prey), copy.deepcopy(input_environment), input_pos)
    _, _, agent_steps, prey_steps, predator_steps, actual_prey_steps, actual_predator_steps= agent_5.move()
    test = animation.Animation(input_environment,prey_steps, predator_steps, agent_steps, actual_prey_steps, actual_predator_steps)

    print('------------------------------------------')
    print('Agent 5')
    print('Agent moves:')
    print(agent_steps)
    print('Prey moves:')
    print(prey_steps)
    print('Predator moves:')
    print(predator_steps)


    agent_7 = ag7.Agent_7(copy.deepcopy(input_predator), copy.deepcopy(input_prey), copy.deepcopy(input_environment), input_pos)
    _, _, agent_steps, prey_steps, predator_steps, actual_prey_steps, actual_predator_steps= agent_7.move()
    test = animation.Animation(input_environment,prey_steps, predator_steps, agent_steps, actual_prey_steps, actual_predator_steps)

    print('------------------------------------------')
    print('Agent 7')
    print('Agent moves:')
    print(agent_steps)
    print('Prey moves:')
    print(prey_steps)
    print('Predator moves:')
    print(predator_steps)


if __name__ == '__main__':
    main()