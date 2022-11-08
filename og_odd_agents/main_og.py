import agent_1_og, agent_1, agent_3_og, agent_3, agent_5_og, agent_5, agent_7_og, agent_7
import prey
import predator
import environment
import random
import copy

def main():

    num_runs = 100
    num_environments = 30
    total_runs = num_runs * num_environments

    a1_og_caught = 0
    a1_og_died = 0
    a1_og_time_out = 0
    a1_og_steps = 0

    a1_caught = 0
    a1_died = 0
    a1_time_out = 0
    a1_steps = 0

    a3_caught = 0
    a3_died = 0
    a3_time_out = 0
    a3_steps = 0

    a3_og_caught = 0
    a3_og_died = 0
    a3_og_time_out = 0
    a3_og_steps = 0

    a5_caught = 0
    a5_died = 0
    a5_time_out = 0
    a5_steps = 0

    a5_og_caught = 0
    a5_og_died = 0
    a5_og_time_out = 0
    a5_og_steps = 0

    a7_caught = 0
    a7_died = 0
    a7_time_out = 0
    a7_steps = 0

    a7_og_caught = 0
    a7_og_died = 0
    a7_og_time_out = 0
    a7_og_steps = 0

    for i in range(num_environments):
        print(f"\nEnvironment: {i}")
        input_environment = environment.Env(50)
        for j in range(num_runs):
            print(f"{j} ", end="", flush=True)

            input_environment = environment.Env(50)
            input_predator = predator.Predator()
            input_prey = prey.Prey() 
            input_pos = random.choice(range(0,49))

            #make sure agent doesnt start in occupied node
            while input_prey.pos == input_pos or input_predator.pos == input_pos:
                input_pos = random.choice(range(0,49))
            
            test_agent_1 = agent_1_og.Agent_1(copy.deepcopy(input_predator), copy.deepcopy(input_prey), copy.deepcopy(input_environment), input_pos)
            k = test_agent_1.move()
            a1_og_steps += k[1]
            result_1_og = k[0]
            if result_1_og == 1:
                a1_og_caught += 1
            elif result_1_og == 0:
                a1_og_died += 1
            elif result_1_og == -1:
                a1_og_time_out +=1

            test_agent_1 = agent_1.Agent_1(copy.deepcopy(input_predator), copy.deepcopy(input_prey), copy.deepcopy(input_environment), input_pos)
            k = test_agent_1.move()
            a1_steps += k[1]
            result_1 = k[0]
            if result_1 == 1:
                a1_caught += 1
            elif result_1 == 0:
                a1_died += 1
            elif result_1 == -1:
                a1_time_out +=1
            
            test_agent_3 = agent_3_og.Agent_3(copy.deepcopy(input_predator), copy.deepcopy(input_prey), copy.deepcopy(input_environment), input_pos)
            k = test_agent_3.move()
            a3_og_steps += k[1]
            result_3_og = k[0]
            if result_3_og == 1:
                a3_og_caught += 1
            elif result_3_og == 0:
                a3_og_died += 1
            elif result_3_og == -1:
                a3_og_time_out +=1
            
            test_agent_3 = agent_3.Agent_3(copy.deepcopy(input_predator), copy.deepcopy(input_prey), copy.deepcopy(input_environment), input_pos)
            k = test_agent_3.move()
            a3_steps += k[1]
            result_3 = k[0]
            if result_3 == 1:
                a3_caught += 1
            elif result_3 == 0:
                a3_died += 1
            elif result_3 == -1:
                a3_time_out +=1
            
            test_agent_5 = agent_5_og.Agent_5(copy.deepcopy(input_predator), copy.deepcopy(input_prey), copy.deepcopy(input_environment), input_pos)
            k = test_agent_5.move()
            a5_og_steps += k[1]
            result_5_og = k[0]
            if result_5_og == 1:
                a5_og_caught += 1
            elif result_5_og == 0:
                a5_og_died += 1
            elif result_5_og == -1:
                a5_og_time_out +=1
            
            test_agent_5 = agent_5.Agent_5(copy.deepcopy(input_predator), copy.deepcopy(input_prey), copy.deepcopy(input_environment), input_pos)
            k = test_agent_5.move()
            a5_steps += k[1]
            result_5 = k[0]
            if result_5 == 1:
                a5_caught += 1
            elif result_5 == 0:
                a5_died += 1
            elif result_5 == -1:
                a5_time_out +=1

            test_agent_7 = agent_7_og.Agent_7(copy.deepcopy(input_predator), copy.deepcopy(input_prey), copy.deepcopy(input_environment), input_pos)
            k = test_agent_7.move()
            a7_og_steps += k[1]
            result_7_og = k[0]
            if result_7_og == 1:
                a7_og_caught += 1
            elif result_7_og == 0:
                a7_og_died += 1
            elif result_7_og == -1:
                a7_og_time_out +=1
            
            test_agent_7 = agent_7.Agent_7(copy.deepcopy(input_predator), copy.deepcopy(input_prey), copy.deepcopy(input_environment), input_pos)
            k = test_agent_7.move()
            a7_steps += k[1]
            result_7 = k[0]
            if result_7 == 1:
                a7_caught += 1
            elif result_7 == 0:
                a7_died += 1
            elif result_7 == -1:
                a7_time_out +=1
            
            
    print()
    print("Compare Original Odd Agents to Optimized (pick any node in best category rather than best overall)")
            
    print("\nAgent 1_og:")
    print(f"Caught (including timeout): {round((a1_og_caught/total_runs) * 100, 3)}% | Died (including timeout): {round((a1_og_died/total_runs) * 100, 3)}% | Timed Out %: {round((a1_og_time_out/total_runs) * 100, 3)}%")
    print(f"Caught (excluding timeout): {round((a1_og_caught/(total_runs-a1_og_time_out)) * 100, 3)}% | Died (exlcuding) timeout): {round((a1_og_died/(total_runs-a1_og_time_out) * 100),3)}% | Avg Steps: {a1_og_steps/total_runs}")

    print("\nAgent 1:")
    print(f"Caught (including timeout): {round((a1_caught/total_runs) * 100, 3)}% | Died (including timeout): {round((a1_died/total_runs) * 100, 3)}% | Timed Out %: {round((a1_time_out/total_runs) * 100, 3)}%")
    print(f"Caught (excluding timeout): {round((a1_caught/(total_runs-a1_time_out)) * 100, 3)}% | Died (exlcuding) timeout): {round((a1_died/(total_runs-a1_time_out) * 100),3)}% | Avg Steps: {a1_steps/total_runs}")

    print("\nAgent 3_og:")
    print(f"Caught (including timeout): {round((a3_og_caught/total_runs) * 100, 3)}% | Died (including timeout): {round((a3_og_died/total_runs) * 100, 3)}% | Timed Out %: {round((a3_og_time_out/total_runs) * 100, 3)}%")
    print(f"Caught (excluding timeout): {round((a3_og_caught/(total_runs-a3_og_time_out)) * 100, 3)}% | Died (exlcuding) timeout): {round((a3_og_died/(total_runs-a3_og_time_out) * 100),3)}% | Avg Steps: {a3_og_steps/total_runs}")

    print("\nAgent 3:")
    print(f"Caught (including timeout): {round((a3_caught/total_runs) * 100, 3)}% | Died (including timeout): {round((a3_died/total_runs) * 100, 3)}% | Timed Out %: {round((a3_time_out/total_runs) * 100, 3)}%")
    print(f"Caught (excluding timeout): {round((a3_caught/(total_runs-a3_time_out)) * 100, 3)}% | Died (exlcuding) timeout): {round((a3_died/(total_runs-a3_time_out) * 100),3)}% | Avg Steps: {a3_steps/total_runs}")

    print("\nAgent 5_og:")
    print(f"Caught (including timeout): {round((a5_og_caught/total_runs) * 100, 3)}% | Died (including timeout): {round((a5_og_died/total_runs) * 100, 3)}% | Timed Out %: {round((a5_og_time_out/total_runs) * 100, 3)}%")
    print(f"Caught (excluding timeout): {round((a5_og_caught/(total_runs-a5_og_time_out)) * 100, 3)}% | Died (exlcuding) timeout): {round((a5_og_died/(total_runs-a5_og_time_out) * 100),3)}% | Avg Steps: {a5_og_steps/total_runs}")

    print("\nAgent 5:")
    print(f"Caught (including timeout): {round((a5_caught/total_runs) * 100, 3)}% | Died (including timeout): {round((a5_died/total_runs) * 100, 3)}% | Timed Out %: {round((a5_time_out/total_runs) * 100, 3)}%")
    print(f"Caught (excluding timeout): {round((a5_caught/(total_runs-a5_time_out)) * 100, 3)}% | Died (exlcuding) timeout): {round((a5_died/(total_runs-a5_time_out) * 100),3)}% | Avg Steps: {a5_steps/total_runs}")

    print("\nAgent 7_og:")
    print(f"Caught (including timeout): {round((a7_og_caught/total_runs) * 100, 3)}% | Died (including timeout): {round((a7_og_died/total_runs) * 100, 3)}% | Timed Out %: {round((a7_og_time_out/total_runs) * 100, 3)}%")
    print(f"Caught (excluding timeout): {round((a7_og_caught/(total_runs-a7_og_time_out)) * 100, 3)}% | Died (exlcuding) timeout): {round((a7_og_died/(total_runs-a7_og_time_out) * 100),3)}% | Avg Steps: {a7_og_steps/total_runs}")

    print("\nAgent 7:")
    print(f"Caught (including timeout): {round((a7_caught/total_runs) * 100, 3)}% | Died (including timeout): {round((a7_died/total_runs) * 100, 3)}% | Timed Out %: {round((a7_time_out/total_runs) * 100, 3)}%")
    print(f"Caught (excluding timeout): {round((a7_caught/(total_runs-a7_time_out)) * 100, 3)}% | Died (exlcuding) timeout): {round((a7_died/(total_runs-a7_time_out) * 100),3)}% | Avg Steps: {a7_steps/total_runs}")

if __name__ == '__main__':
    main()