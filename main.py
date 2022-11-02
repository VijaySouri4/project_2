import agent_1, agent_2, agent_3, agent_4, agent_5, agent_6, agent_7, agent_8, agent_7_defect, agent_8_defect
import prey
import predator
import environment
import random
import copy

def main():

    num_runs = 45
    num_environments = 30
    total_runs = num_runs * num_environments

    a1_caught = 0
    a1_died = 0
    a1_time_out = 0
    a1_steps = 0

    a2_caught = 0
    a2_died = 0
    a2_time_out = 0
    a2_steps = 0

    a3_caught = 0
    a3_died = 0
    a3_time_out = 0
    a3_steps = 0

    a4_caught = 0
    a4_died = 0
    a4_time_out = 0
    a4_steps = 0

    a5_caught = 0
    a5_died = 0
    a5_time_out = 0
    a5_steps = 0

    a6_caught = 0
    a6_died = 0
    a6_time_out = 0
    a6_steps = 0

    a7_caught = 0
    a7_died = 0
    a7_time_out = 0
    a7_steps = 0

    a7d_caught = 0
    a7d_died = 0
    a7d_time_out = 0
    a7d_steps = 0

    a8_caught = 0
    a8_died = 0
    a8_time_out = 0
    a8_steps = 0

    a8d_caught = 0
    a8d_died = 0
    a8d_time_out = 0
    a8d_steps = 0

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
            
            test_agent_1 = agent_1.Agent_1(copy.deepcopy(input_predator), copy.deepcopy(input_prey), copy.deepcopy(input_environment), input_pos)
            result_1, steps = test_agent_1.move()
            a1_steps += steps
            if result_1 == 1:
                a1_caught += 1
            elif result_1 == 0:
                a1_died += 1
            elif result_1 == -1:
                a1_time_out +=1
            
            test_agent_2 = agent_2.Agent_2(copy.deepcopy(input_predator), copy.deepcopy(input_prey), copy.deepcopy(input_environment), input_pos)
            result_2, steps = test_agent_2.move()
            a2_steps += steps
            if result_2 == 1:
                a2_caught += 1
            elif result_2 == 0:
                a2_died += 1
            elif result_2 == -1:
                a2_time_out +=1
            
            test_agent_3 = agent_3.Agent_3(copy.deepcopy(input_predator), copy.deepcopy(input_prey), copy.deepcopy(input_environment), input_pos)
            result_3, steps = test_agent_3.move()
            a3_steps += steps
            if result_3 == 1:
                a3_caught += 1
            elif result_3 == 0:
                a3_died += 1
            elif result_3 == -1:
                a3_time_out +=1
            
            test_agent_4 = agent_4.Agent_4(copy.deepcopy(input_predator), copy.deepcopy(input_prey), copy.deepcopy(input_environment), input_pos)
            result_4, steps = test_agent_4.move()
            a4_steps += steps
            if result_4 == 1:
                a4_caught += 1
            elif result_4 == 0:
                a4_died += 1
            elif result_4 == -1:
                a4_time_out +=1
            
            test_agent_5 = agent_5.Agent_5(copy.deepcopy(input_predator), copy.deepcopy(input_prey), copy.deepcopy(input_environment), input_pos)
            result_5, steps = test_agent_5.move()
            a5_steps += steps
            if result_5 == 1:
                a5_caught += 1
            elif result_5 == 0:
                a5_died += 1
            elif result_5 == -1:
                a5_time_out +=1
            
            test_agent_6 = agent_6.Agent_6(copy.deepcopy(input_predator), copy.deepcopy(input_prey), copy.deepcopy(input_environment), input_pos)
            result_6, steps = test_agent_6.move()
            a6_steps += steps
            if result_6 == 1:
                a6_caught += 1
            elif result_6 == 0:
                a6_died += 1
            elif result_6 == -1:
                a6_time_out +=1
            
            test_agent_7 = agent_7.Agent_7(copy.deepcopy(input_predator), copy.deepcopy(input_prey), copy.deepcopy(input_environment), input_pos)
            result_7, steps = test_agent_7.move()
            a7_steps += steps
            if result_7 == 1:
                a7_caught += 1
            elif result_7 == 0:
                a7_died += 1
            elif result_7 == -1:
                a7_time_out +=1

            test_agent_7_defect = agent_7_defect.Agent_7_defect(copy.deepcopy(input_predator), copy.deepcopy(input_prey), copy.deepcopy(input_environment), input_pos)
            result_7_defect, steps = test_agent_7_defect.move()
            a7d_steps += steps
            if result_7_defect == 1:
                a7d_caught += 1
            elif result_7_defect == 0:
                a7d_died += 1
            elif result_7_defect == -1:
                a7d_time_out +=1
            
            test_agent_8 = agent_8.Agent_8(copy.deepcopy(input_predator), copy.deepcopy(input_prey), copy.deepcopy(input_environment), input_pos)
            result_8, steps = test_agent_8.move()
            a8_steps += steps
            if result_8 == 1:
                a8_caught += 1
            elif result_8 == 0:
                a8_died += 1
            elif result_8 == -1:
                a8_time_out +=1

            test_agent_8_defect = agent_8_defect.Agent_8_defect(copy.deepcopy(input_predator), copy.deepcopy(input_prey), copy.deepcopy(input_environment), input_pos)
            result_8_defect, steps = test_agent_8_defect.move()
            a8d_steps += steps
            if result_8_defect == 1:
                a8d_caught += 1
            elif result_8_defect == 0:
                a8d_died += 1
            elif result_8_defect == -1:
                a8d_time_out +=1
            
    print()
            
    print("\nAgent 1:")
    print(f"Caught (including timeout): {round((a1_caught/total_runs) * 100, 3)}% | Died (including timeout): {round((a1_died/total_runs) * 100, 3)}% | Timed Out %: {round((a1_time_out/total_runs) * 100, 3)}%")
    print(f"Caught (excluding timeout): {round((a1_caught/(total_runs-a1_time_out)) * 100, 3)}% | Died (exlcuding) timeout): {round((a1_died/(total_runs-a1_time_out) * 100),3)}% | Avg Steps: {a1_steps/total_runs}")

    print("\nAgent 2:")
    print(f"Caught (including timeout): {round((a2_caught/total_runs) * 100, 3)}% | Died (including timeout): {round((a2_died/total_runs) * 100, 3)}% | Timed Out %: {round((a2_time_out/total_runs) * 100, 3)}%")
    print(f"Caught (excluding timeout): {round((a2_caught/(total_runs-a2_time_out)) * 100, 3)}% | Died (exlcuding) timeout): {round((a2_died/(total_runs-a2_time_out) * 100),3)}% | Avg Steps: {a2_steps/total_runs}")

    print("\nAgent 3:")
    print(f"Caught (including timeout): {round((a3_caught/total_runs) * 100, 3)}% | Died (including timeout): {round((a3_died/total_runs) * 100, 3)}% | Timed Out %: {round((a3_time_out/total_runs) * 100, 3)}%")
    print(f"Caught (excluding timeout): {round((a3_caught/(total_runs-a3_time_out)) * 100, 3)}% | Died (exlcuding) timeout): {round((a3_died/(total_runs-a3_time_out) * 100),3)}% | Avg Steps: {a3_steps/total_runs}")

    print("\nAgent 4:")
    print(f"Caught (including timeout): {round((a4_caught/total_runs) * 100, 3)}% | Died (including timeout): {round((a4_died/total_runs) * 100, 3)}% | Timed Out %: {round((a4_time_out/total_runs) * 100, 3)}%")
    print(f"Caught (excluding timeout): {round((a4_caught/(total_runs-a4_time_out)) * 100, 3)}% | Died (exlcuding) timeout): {round((a4_died/(total_runs-a4_time_out) * 100),3)}% | Avg Steps: {a4_steps/total_runs}")


    print("\nAgent 5:")
    print(f"Caught (including timeout): {round((a5_caught/total_runs) * 100, 3)}% | Died (including timeout): {round((a5_died/total_runs) * 100, 3)}% | Timed Out %: {round((a5_time_out/total_runs) * 100, 3)}%")
    print(f"Caught (excluding timeout): {round((a5_caught/(total_runs-a5_time_out)) * 100, 3)}% | Died (exlcuding) timeout): {round((a5_died/(total_runs-a5_time_out) * 100),3)}% | Avg Steps: {a5_steps/total_runs}")

    print("\nAgent 6:")
    print(f"Caught (including timeout): {round((a6_caught/total_runs) * 100, 3)}% | Died (including timeout): {round((a6_died/total_runs) * 100, 3)}% | Timed Out %: {round((a6_time_out/total_runs) * 100, 3)}%")
    print(f"Caught (excluding timeout): {round((a6_caught/(total_runs-a6_time_out)) * 100, 3)}% | Died (exlcuding) timeout): {round((a6_died/(total_runs-a6_time_out) * 100),3)}% | Avg Steps: {a6_steps/total_runs}")

    print("\nAgent 7:")
    print(f"Caught (including timeout): {round((a7_caught/total_runs) * 100, 3)}% | Died (including timeout): {round((a7_died/total_runs) * 100, 3)}% | Timed Out %: {round((a7_time_out/total_runs) * 100, 3)}%")
    print(f"Caught (excluding timeout): {round((a7_caught/(total_runs-a7_time_out)) * 100, 3)}% | Died (exlcuding) timeout): {round((a7_died/(total_runs-a7_time_out) * 100),3)}% | Avg Steps: {a7_steps/total_runs}")

    print("\nAgent 7 Defective:")
    print(f"Caught (including timeout): {round((a7d_caught/total_runs) * 100, 3)}% | Died (including timeout): {round((a7d_died/total_runs) * 100, 3)}% | Timed Out %: {round((a7d_time_out/total_runs) * 100, 3)}%")
    print(f"Caught (excluding timeout): {round((a7d_caught/(total_runs-a7d_time_out)) * 100, 3)}% | Died (exlcuding) timeout): {round((a7d_died/(total_runs-a7d_time_out) * 100),3)}% | Avg Steps: {a7d_steps/total_runs}")

    print("\nAgent 8:")
    print(f"Caught (including timeout): {round((a8_caught/total_runs) * 100, 3)}% | Died (including timeout): {round((a8_died/total_runs) * 100, 3)}% | Timed Out %: {round((a8_time_out/total_runs) * 100, 3)}%")
    print(f"Caught (excluding timeout): {round((a8_caught/(total_runs-a8_time_out)) * 100, 3)}% | Died (exlcuding) timeout): {round((a8_died/(total_runs-a8_time_out) * 100),3)}% | Avg Steps: {a8_steps/total_runs}")

    print("\nAgent 8 Defective:")
    print(f"Caught (including timeout): {round((a8d_caught/total_runs) * 100, 3)}% | Died (including timeout): {round((a8d_died/total_runs) * 100, 3)}% | Timed Out %: {round((a8d_time_out/total_runs) * 100, 3)}%")
    print(f"Caught (excluding timeout): {round((a8d_caught/(total_runs-a8d_time_out)) * 100, 3)}% | Died (exlcuding) timeout): {round((a8d_died/(total_runs-a8d_time_out) * 100),3)}% | Avg Steps: {a8d_steps/total_runs}")

if __name__ == '__main__':
    main()