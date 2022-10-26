import agent_1, agent_2, agent_2_type2
import prey
import predator
import environment
import random
import copy

def main():

    total_runs = 3000

    a1_caught = 0
    a1_died = 0
    a1_time_out = 0
    a1_steps = 0

    a2_caught = 0
    a2_died = 0
    a2_time_out = 0

    for i in range(total_runs):
        print(f"{i} ", end="", flush=True)

        input_environment = environment.Env(50)
        input_predator = predator.Predator()
        input_prey = prey.Prey() 
        input_pos = random.choice(range(0,49))

        #make sure agent doesnt start in occupied node
        while input_prey.pos == input_pos or input_predator.pos == input_pos:
            input_pos = random.choice(range(0,49))

        test_agent_1 = agent_1.Agent_1(copy.deepcopy(input_predator), copy.deepcopy(input_prey), copy.deepcopy(input_environment), input_pos)
        result_1, steps = test_agent_1.move()
        a1_steps += steps
        if result_1 == 1:
            a1_caught += 1
        elif result_1 == 0:
            a1_died += 1
        elif result_1 == -1:
            a1_time_out +=1
        
        test_agent_2 = agent_2_type2.Agent_2_2(copy.deepcopy(input_predator), copy.deepcopy(input_prey), copy.deepcopy(input_environment), input_pos)
        #result = test_agent_2.move()
        #result_2 = test_agent_2.move()
        result_2 = 0
        if result_2 == 1:
            a2_caught += 1
        elif result_2 == 0:
            a2_died += 1
        elif result_2 == -1:
            a2_time_out +=1

    print()
            
    print("\nAgent 1:")
    print(f"Caught (including timeout): {round((a1_caught/total_runs) * 100, 3)}% | Died (including timeout): {round((a1_died/total_runs) * 100, 3)}% | Timed Out %: {round((a1_time_out/total_runs) * 100, 3)}%")
    print(f"Caught (excluding timeout): {round((a1_caught/(total_runs-a1_time_out)) * 100, 3)}% | Died (exlcuding) timeout): {round((a1_died/(total_runs-a1_time_out) * 100),3)}% | Avg Steps: {a1_steps/total_runs}")

    print("\nAgent 2:")
    print(f"Caught (including timeout): {round((a2_caught/total_runs) * 100, 3)}% | Died (including timeout): {round((a2_died/total_runs) * 100, 3)}% | Timed Out %: {round((a2_time_out/total_runs) * 100, 3)}%")
    print(f"Caught (excluding timeout): {round((a2_caught/(total_runs-a2_time_out)) * 100, 3)}% | Died (exlcuding) timeout): {round((a2_died/(total_runs-a2_time_out) * 100),3)}%")
if __name__ == '__main__':
    main()