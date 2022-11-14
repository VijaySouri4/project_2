import agent_1, agent_2, agent_3, agent_4, agent_5, agent_6, agent_7, agent_8, agent_7_defect, agent_8_defect, agent_7_defect_updated, agent_8_defect_updated
import prey
import predator
import environment
import random
import numpy as np
import copy
import matplotlib.pyplot as plt

def main():

    num_runs = 3
    num_environments = 3
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
    a3_prey_certain = 0

    a4_caught = 0
    a4_died = 0
    a4_time_out = 0
    a4_steps = 0
    a4_prey_certain = 0

    a5_caught = 0
    a5_died = 0
    a5_time_out = 0
    a5_steps = 0
    a5_predator_certain = 0

    a6_caught = 0
    a6_died = 0
    a6_time_out = 0
    a6_steps = 0
    a6_predator_certain = 0

    a7_caught = 0
    a7_died = 0
    a7_time_out = 0
    a7_steps = 0
    a7_prey_certain = 0
    a7_predator_certain = 0

    a7d_caught = 0
    a7d_died = 0
    a7d_time_out = 0
    a7d_steps = 0
    a7d_prey_certain = 0
    a7d_predator_certain = 0

    a7du_caught = 0
    a7du_died = 0
    a7du_time_out = 0
    a7du_steps = 0
    a7du_prey_certain = 0
    a7du_predator_certain = 0

    a8_caught = 0
    a8_died = 0
    a8_time_out = 0
    a8_steps = 0
    a8_prey_certain = 0
    a8_predator_certain = 0

    a8d_caught = 0
    a8d_died = 0
    a8d_time_out = 0
    a8d_steps = 0
    a8d_prey_certain = 0
    a8d_predator_certain = 0

    a8du_caught = 0
    a8du_died = 0
    a8du_time_out = 0
    a8du_steps = 0
    a8du_prey_certain = 0
    a8du_predator_certain = 0

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
            k = test_agent_1.move()
            a1_steps += k[1]
            result_1 = k[0]
            if result_1 == 1:
                a1_caught += 1
            elif result_1 == 0:
                a1_died += 1
            elif result_1 == -1:
                a1_time_out +=1
            
            test_agent_2 = agent_2.Agent_2(copy.deepcopy(input_predator), copy.deepcopy(input_prey), copy.deepcopy(input_environment), input_pos)
            k = test_agent_2.move()
            a2_steps += k[1]
            result_2 = k[0]
            if result_2 == 1:
                a2_caught += 1
            elif result_2 == 0:
                a2_died += 1
            elif result_2 == -1:
                a2_time_out +=1
            
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
            a3_prey_certain += test_agent_3.certain_prey_pos
            
            test_agent_4 = agent_4.Agent_4(copy.deepcopy(input_predator), copy.deepcopy(input_prey), copy.deepcopy(input_environment), input_pos)
            k = test_agent_4.move()
            a4_steps += k[1]
            result_4 = k[0]
            if result_4 == 1:
                a4_caught += 1
            elif result_4 == 0:
                a4_died += 1
            elif result_4 == -1:
                a4_time_out +=1
            a4_prey_certain += test_agent_4.certain_prey_pos
            
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
            a5_predator_certain += test_agent_5.certain_predator_pos
            
            test_agent_6 = agent_6.Agent_6(copy.deepcopy(input_predator), copy.deepcopy(input_prey), copy.deepcopy(input_environment), input_pos)
            k = test_agent_6.move()
            a6_steps += k[1]
            result_6 = k[0]
            if result_6 == 1:
                a6_caught += 1
            elif result_6 == 0:
                a6_died += 1
            elif result_6 == -1:
                a6_time_out +=1
            a6_predator_certain += test_agent_6.certain_predator_pos
            

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
            a7_prey_certain += test_agent_7.certain_prey_pos
            a7_predator_certain += test_agent_7.certain_predator_pos
            
            test_agent_7_defect = agent_7_defect.Agent_7_defect(copy.deepcopy(input_predator), copy.deepcopy(input_prey), copy.deepcopy(input_environment), input_pos)
            k = test_agent_7_defect.move()
            a7d_steps += k[1]
            result_7_defect = k[0]
            if result_7_defect == 1:
                a7d_caught += 1
            elif result_7_defect == 0:
                a7d_died += 1
            elif result_7_defect == -1:
                a7d_time_out +=1
            a7d_prey_certain += test_agent_7_defect.certain_prey_pos
            a7d_predator_certain += test_agent_7_defect.certain_predator_pos

            test_agent_7_defect_updated = agent_7_defect_updated.Agent_7_defect_updated(copy.deepcopy(input_predator), copy.deepcopy(input_prey), copy.deepcopy(input_environment), input_pos)
            k = test_agent_7_defect_updated.move()
            a7du_steps += k[1]
            result_7_defect_updated = k[0]
            if result_7_defect_updated == 1:
                a7du_caught += 1
            elif result_7_defect_updated == 0:
                a7du_died += 1
            elif result_7_defect_updated == -1:
                a7du_time_out +=1
            a7du_prey_certain += test_agent_7_defect_updated.certain_prey_pos
            a7du_predator_certain += test_agent_7_defect_updated.certain_predator_pos
            
            test_agent_8 = agent_8.Agent_8(copy.deepcopy(input_predator), copy.deepcopy(input_prey), copy.deepcopy(input_environment), input_pos)
            k = test_agent_8.move()
            a8_steps += k[1]
            result_8 = k[0]
            if result_8 == 1:
                a8_caught += 1
            elif result_8 == 0:
                a8_died += 1
            elif result_8 == -1:
                a8_time_out +=1
            a8_prey_certain += test_agent_8.certain_prey_pos
            a8_predator_certain += test_agent_8.certain_predator_pos
            
            test_agent_8_defect = agent_8_defect.Agent_8_defect(copy.deepcopy(input_predator), copy.deepcopy(input_prey), copy.deepcopy(input_environment), input_pos)
            k = test_agent_8_defect.move()
            a8d_steps += k[1]
            result_8_defect = k[0]
            if result_8_defect == 1:
                a8d_caught += 1
            elif result_8_defect == 0:
                a8d_died += 1
            elif result_8_defect == -1:
                a8d_time_out +=1
            a8d_prey_certain += test_agent_8_defect.certain_prey_pos
            a8d_predator_certain += test_agent_8_defect.certain_predator_pos

            test_agent_8_defect_updated = agent_8_defect_updated.Agent_8_defect_updated(copy.deepcopy(input_predator), copy.deepcopy(input_prey), copy.deepcopy(input_environment), input_pos)
            k = test_agent_8_defect_updated.move()
            a8du_steps += k[1]
            result_8_defect_updated = k[0]
            if result_8_defect_updated == 1:
                a8du_caught += 1
            elif result_8_defect_updated == 0:
                a8du_died += 1
            elif result_8_defect_updated == -1:
                a8du_time_out +=1
            a8du_prey_certain += test_agent_8_defect_updated.certain_prey_pos
            a8du_predator_certain += test_agent_8_defect_updated.certain_predator_pos
            
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
    print(f"Steps where certain of prey pos (and correct): {round(a3_prey_certain/a3_steps * 100, 3)}%")

    print("\nAgent 4:")
    print(f"Caught (including timeout): {round((a4_caught/total_runs) * 100, 3)}% | Died (including timeout): {round((a4_died/total_runs) * 100, 3)}% | Timed Out %: {round((a4_time_out/total_runs) * 100, 3)}%")
    print(f"Caught (excluding timeout): {round((a4_caught/(total_runs-a4_time_out)) * 100, 3)}% | Died (exlcuding) timeout): {round((a4_died/(total_runs-a4_time_out) * 100),3)}% | Avg Steps: {a4_steps/total_runs}")
    print(f"Steps where certain of prey pos (and correct): {round(a4_prey_certain/a4_steps * 100, 3)}%")

    print("\nAgent 5:")
    print(f"Caught (including timeout): {round((a5_caught/total_runs) * 100, 3)}% | Died (including timeout): {round((a5_died/total_runs) * 100, 3)}% | Timed Out %: {round((a5_time_out/total_runs) * 100, 3)}%")
    print(f"Caught (excluding timeout): {round((a5_caught/(total_runs-a5_time_out)) * 100, 3)}% | Died (exlcuding) timeout): {round((a5_died/(total_runs-a5_time_out) * 100),3)}% | Avg Steps: {a5_steps/total_runs}")
    print(f"Steps where certain of predator pos (and correct): {round(a5_predator_certain/a5_steps * 100, 3)}%")

    print("\nAgent 6:")
    print(f"Caught (including timeout): {round((a6_caught/total_runs) * 100, 3)}% | Died (including timeout): {round((a6_died/total_runs) * 100, 3)}% | Timed Out %: {round((a6_time_out/total_runs) * 100, 3)}%")
    print(f"Caught (excluding timeout): {round((a6_caught/(total_runs-a6_time_out)) * 100, 3)}% | Died (exlcuding) timeout): {round((a6_died/(total_runs-a6_time_out) * 100),3)}% | Avg Steps: {a6_steps/total_runs}")
    print(f"Steps where certain of predator pos (and correct): {round(a6_predator_certain/a6_steps * 100, 3)}%")

    print("\nAgent 7:")
    print(f"Caught (including timeout): {round((a7_caught/total_runs) * 100, 3)}% | Died (including timeout): {round((a7_died/total_runs) * 100, 3)}% | Timed Out %: {round((a7_time_out/total_runs) * 100, 3)}%")
    print(f"Caught (excluding timeout): {round((a7_caught/(total_runs-a7_time_out)) * 100, 3)}% | Died (exlcuding) timeout): {round((a7_died/(total_runs-a7_time_out) * 100),3)}% | Avg Steps: {a7_steps/total_runs}")
    print(f"Steps where certain of prey pos (and correct): {round(a7_prey_certain/a7_steps * 100, 3)}")
    print(f"Steps where certain of predator pos (and correct): {round(a7_predator_certain/a7_steps * 100, 3)}%")

    print("\nAgent 7 Defective:")
    print(f"Caught (including timeout): {round((a7d_caught/total_runs) * 100, 3)}% | Died (including timeout): {round((a7d_died/total_runs) * 100, 3)}% | Timed Out %: {round((a7d_time_out/total_runs) * 100, 3)}%")
    print(f"Caught (excluding timeout): {round((a7d_caught/(total_runs-a7d_time_out)) * 100, 3)}% | Died (exlcuding) timeout): {round((a7d_died/(total_runs-a7d_time_out) * 100),3)}% | Avg Steps: {a7d_steps/total_runs}")
    print(f"Steps where certain of prey pos (and correct): {round(a7d_prey_certain/a7d_steps * 100, 3)}%")
    print(f"Steps where certain of predator pos (and correct): {round(a7d_predator_certain/a7d_steps * 100, 3)}%")

    print("\nAgent 7 Defective Updated:")
    print(f"Caught (including timeout): {round((a7du_caught/total_runs) * 100, 3)}% | Died (including timeout): {round((a7du_died/total_runs) * 100, 3)}% | Timed Out %: {round((a7du_time_out/total_runs) * 100, 3)}%")
    print(f"Caught (excluding timeout): {round((a7du_caught/(total_runs-a7du_time_out)) * 100, 3)}% | Died (exlcuding) timeout): {round((a7du_died/(total_runs-a7du_time_out) * 100),3)}% | Avg Steps: {a7du_steps/total_runs}")
    print(f"Steps where certain of prey pos (and correct): {round(a7du_prey_certain/a7du_steps * 100, 3)}%")
    print(f"Steps where certain of predator pos (and correct): {round(a7du_predator_certain/a7du_steps * 100, 3)}%")

    print("\nAgent 8:")
    print(f"Caught (including timeout): {round((a8_caught/total_runs) * 100, 3)}% | Died (including timeout): {round((a8_died/total_runs) * 100, 3)}% | Timed Out %: {round((a8_time_out/total_runs) * 100, 3)}%")
    print(f"Caught (excluding timeout): {round((a8_caught/(total_runs-a8_time_out)) * 100, 3)}% | Died (exlcuding) timeout): {round((a8_died/(total_runs-a8_time_out) * 100),3)}% | Avg Steps: {a8_steps/total_runs}")
    print(f"Steps where certain of prey pos (and correct): {round(a8_prey_certain/a8_steps * 100, 3)}%")
    print(f"Steps where certain of predator pos (and correct): {round(a8_predator_certain/a8_steps * 100, 3)}%")

    print("\nAgent 8 Defective:")
    print(f"Caught (including timeout): {round((a8d_caught/total_runs) * 100, 3)}% | Died (including timeout): {round((a8d_died/total_runs) * 100, 3)}% | Timed Out %: {round((a8d_time_out/total_runs) * 100, 3)}%")
    print(f"Caught (excluding timeout): {round((a8d_caught/(total_runs-a8d_time_out)) * 100, 3)}% | Died (exlcuding) timeout): {round((a8d_died/(total_runs-a8d_time_out) * 100),3)}% | Avg Steps: {a8d_steps/total_runs}")
    print(f"Steps where certain of prey pos (and correct): {round(a8d_prey_certain/a8d_steps * 100, 3)}%")
    print(f"Steps where certain of predator pos (and correct): {round(a8d_predator_certain/a8d_steps * 100, 3)}%")

    print("\nAgent 8 Defective Updated:")
    print(f"Caught (including timeout): {round((a8du_caught/total_runs) * 100, 3)}% | Died (including timeout): {round((a8du_died/total_runs) * 100, 3)}% | Timed Out %: {round((a8du_time_out/total_runs) * 100, 3)}%")
    print(f"Caught (excluding timeout): {round((a8du_caught/(total_runs-a8du_time_out)) * 100, 3)}% | Died (exlcuding) timeout): {round((a8du_died/(total_runs-a8du_time_out) * 100),3)}% | Avg Steps: {a8du_steps/total_runs}")
    print(f"Steps where certain of prey pos (and correct): {round(a8du_prey_certain/a8du_steps * 100, 3)}%")
    print(f"Steps where certain of predator pos (and correct): {round(a8du_predator_certain/a8du_steps * 100, 3)}%") 


    caught_data = {'Agent 1':round((a1_caught/total_runs) * 100, 3), 'Agent 2':round((a2_caught/total_runs) * 100, 3),
     'Agent 3':round((a3_caught/total_runs) * 100, 3), 'Agent 4':round((a4_caught/total_runs) * 100, 3),
      'Agent 5':round((a5_caught/total_runs) * 100, 3),
       'Agent 6':round((a6_caught/total_runs) * 100, 3),
        'Agent 7':round((a7_caught/total_runs) * 100, 3),
         'Agent 7 Defective':round((a7d_caught/total_runs) * 100, 3),
          'Agent 7 Defective Updated':round((a7du_caught/total_runs) * 100, 3),
           'Agent 8':round((a8_caught/total_runs) * 100, 3),
            'Agent 8 Defective':round((a8d_caught/total_runs) * 100, 3),
             'Agent 8 Defective Updated':round((a7du_caught/total_runs) * 100, 3)}

    death_data = {'Agent 1':round((a1_died/total_runs) * 100, 3),
     'Agent 2':round((a2_died/total_runs) * 100, 3),
     'Agent 3':round((a3_died/total_runs) * 100, 3),
      'Agent 4':round((a4_died/total_runs) * 100, 3),
      'Agent 5':round((a5_died/total_runs) * 100, 3),
       'Agent 6':round((a6_died/total_runs) * 100, 3),
        'Agent 7':round((a7_died/total_runs) * 100, 3),
         'Agent 7 Defective':round((a7d_died/total_runs) * 100, 3),
          'Agent 7 Defective Updated':round((a7du_died/total_runs) * 100, 3),
           'Agent 8':round((a8_died/total_runs) * 100, 3),
            'Agent 8 Defective':round((a8d_died/total_runs) * 100, 3),
             'Agent 8 Defective Updated':round((a7du_died/total_runs) * 100, 3)}

    time_out_data = {'Agent 1':round((a1_time_out/total_runs) * 100, 3),
     'Agent 2':round((a2_time_out/total_runs) * 100, 3),
     'Agent 3':round((a3_time_out/total_runs) * 100, 3),
      'Agent 4':round((a4_time_out/total_runs) * 100, 3),
      'Agent 5':round((a5_time_out/total_runs) * 100, 3),
       'Agent 6':round((a6_time_out/total_runs) * 100, 3),
        'Agent 7':round((a7_time_out/total_runs) * 100, 3),
         'Agent 7 Defective':round((a7d_time_out/total_runs) * 100, 3),
          'Agent 7 Defective Updated':round((a7du_time_out/total_runs) * 100, 3),
           'Agent 8':round((a8_time_out/total_runs) * 100, 3),
            'Agent 8 Defective':round((a8d_time_out/total_runs) * 100, 3),
             'Agent 8 Defective Updated':round((a7du_time_out/total_runs) * 100, 3)}

    steps_data = {'Agent 1':(a1_steps/total_runs),
     'Agent 2':(a2_steps/total_runs),
     'Agent 3':(a3_steps/total_runs),
      'Agent 4':(a4_steps/total_runs),
      'Agent 5':(a5_steps/total_runs),
       'Agent 6':(a6_steps/total_runs),
        'Agent 7':(a7_steps/total_runs),
         'Agent 7 Defective':(a7d_steps/total_runs),
          'Agent 7 Defective Updated':(a7du_steps/total_runs),
           'Agent 8':(a8_steps/total_runs),
            'Agent 8 Defective':(a8d_steps/total_runs),
             'Agent 8 Defective Updated':(a8du_steps/total_runs)}

    prey_certainty_data = {
        'Agent 3':round(a3_prey_certain/a3_steps * 100, 3),
        'Agent 4':round(a4_prey_certain/a4_steps * 100, 3),
        'Agent 7':round(a7_prey_certain/a7_steps * 100, 3),
        'Agent 7\nDefective':round(a7d_prey_certain/a7d_steps * 100, 3),
        'Agent 7\nDefective\nUpdated':round(a7du_prey_certain/a7du_steps * 100, 3),
        'Agent 8':round(a8_prey_certain/a8_steps * 100, 3),
        'Agent 8\nDefective':round(a8d_prey_certain/a8d_steps * 100, 3),
        'Agent 8\nDefective\nUpdated':round(a8du_prey_certain/a8du_steps * 100, 3)}

    predator_certainty_data = {
        'Agent 5':round(a5_predator_certain/a5_steps * 100, 3),
        'Agent 6':round(a6_predator_certain/a6_steps * 100, 3),
        'Agent 7':round(a7_predator_certain/a7_steps * 100, 3),
        'Agent 7\nDefective':round(a7d_predator_certain/a7d_steps * 100, 3),
        'Agent 7\nDefective\nUpdated':round(a7du_predator_certain/a7du_steps * 100, 3),
        'Agent 8':round(a8_predator_certain/a8_steps * 100, 3),
        'Agent 8\nDefective':round(a8d_predator_certain/a8d_steps * 100, 3),
        'Agent 8\nDefective\nUpdated':round(a7du_predator_certain/a8du_steps * 100, 3)}
             
    
    Catch_rates = list(caught_data.values())
    Death_rates = list(death_data.values())
    Time_Out_rates = list(time_out_data.values())
    Steps_rates = list(steps_data.values())
    Agent_names = list(caught_data.keys())
    Prey_certain_agents = list(prey_certainty_data.keys())
    Prey_certain = list(prey_certainty_data.values())
    Predator_certain_agents = list(predator_certainty_data.keys())
    Predator_certain = list(predator_certainty_data.values())
    ## Plots for complete information setting

    fig_complete_info = plt.figure(figsize = (10, 7), dpi=80)

    plt.bar(Agent_names[:2], Catch_rates[:2], color ='green',
            width = 0.2)
    plt.bar(Agent_names[:2], Death_rates[:2], color ='maroon',
            width = 0.4)
    plt.bar(Agent_names[:2], Time_Out_rates[:2], color ='yellow',
            width = 0.6)

    plt.xlabel("Agents")
    plt.ylabel("Success percentage")
    plt.title("Comparision of Success rates of different Agents:")
    #plt.show() 
    fig_complete_info.savefig('/home/vijay/Rutgers/course_work/520/Reports/project_2_plots/Plot1_complete_information_setting.png')

    fig_complete_info_steps = plt.figure(figsize= (10,7), dpi = 100)

    plt.bar(Agent_names[:2], Steps_rates[:2], color ='brown',
            width = 0.2)

    plt.xlabel("Agents")
    plt.ylabel("Average Number of Steps")
    plt.title("Comparision of average number of steps for Complete Information setting:")
    #plt.show() 

    fig_complete_info_steps.savefig('/home/vijay/Rutgers/course_work/520/Reports/project_2_plots/Plot2_complete_information_setting.png')


    ## Plots for Partial Prey information setting 

    fig_partial_prey = plt.figure(figsize = (10, 7), dpi=80)

    plt.bar(Agent_names[2:4], Catch_rates[2:4], color ='green',
            width = 0.2)
    plt.bar(Agent_names[2:4], Death_rates[2:4], color ='maroon',
            width = 0.4)
    plt.bar(Agent_names[2:4], Time_Out_rates[2:4], color ='yellow',
            width = 0.6)

    plt.xlabel("Agents")
    plt.ylabel("Success percentage")
    plt.title("Comparision of Success rates of different Agents:")
    #plt.show() 
    fig_partial_prey.savefig('/home/vijay/Rutgers/course_work/520/Reports/project_2_plots/Plot1_partial_prey_information_setting.png')

    fig_partial_prey_steps = plt.figure(figsize= (10,7), dpi = 100)

    plt.bar(Agent_names[2:4], Steps_rates[2:4], color ='brown',
            width = 0.2)

    plt.xlabel("Agents")
    plt.ylabel("Average Number of Steps")
    plt.title("Comparision of average number of steps for Complete Information setting:")
    #plt.show() 

    fig_partial_prey_steps.savefig('/home/vijay/Rutgers/course_work/520/Reports/project_2_plots/Plot2_partial_prey_information_setting.png')

    ## Plots for Partial predator setting 

    fig_partial_predator = plt.figure(figsize = (10, 7), dpi=80)

    plt.bar(Agent_names[4:6], Catch_rates[4:6], color ='green',
            width = 0.2)
    plt.bar(Agent_names[4:6], Death_rates[4:6], color ='maroon',
            width = 0.4)
    plt.bar(Agent_names[4:6], Time_Out_rates[4:6], color ='yellow',
            width = 0.6)

    plt.xlabel("Agents")
    plt.ylabel("Success percentage")
    plt.title("Comparision of Success rates of different Agents:")
    #plt.show() 
    fig_partial_predator.savefig('/home/vijay/Rutgers/course_work/520/Reports/project_2_plots/Plot1_partial_predator_information_setting.png')

    fig_partial_predator_steps = plt.figure(figsize= (10,7), dpi = 100)

    plt.bar(Agent_names[4:6], Steps_rates[4:6], color ='brown',
            width = 0.2)

    plt.xlabel("Agents")
    plt.ylabel("Average Number of Steps")
    plt.title("Comparision of average number of steps for Complete Information setting:")
    #plt.show() 

    fig_partial_predator_steps.savefig('/home/vijay/Rutgers/course_work/520/Reports/project_2_plots/Plot2_partial_predator_information_setting.png')

    ## Plots for combined partial setting

    fig_combined_partial = plt.figure(figsize = (15, 7), dpi=80)

    plt.bar(Agent_names[6:12], Catch_rates[6:12], color ='green',
            width = 0.2)
    plt.bar(Agent_names[6:12], Death_rates[6:12], color ='maroon',
            width = 0.4)
    plt.bar(Agent_names[6:12], Time_Out_rates[6:12], color ='yellow',
            width = 0.6)

    plt.xlabel("Agents")
    plt.ylabel("Success percentage")
    plt.title("Comparision of Success rates of different Agents:")
    plt.show() 
    fig_combined_partial.savefig('/home/vijay/Rutgers/course_work/520/Reports/project_2_plots/Plot1_combined_information_setting.png')

    fig_combined_partial_steps = plt.figure(figsize= (15,7), dpi = 100)

    plt.bar(Agent_names[6:12], Steps_rates[6:12], color ='brown',
            width = 0.2)

    plt.xlabel("Agents")
    plt.ylabel("Average Number of Steps")
    plt.title("Comparision of average number of steps for Complete Information setting:")
    #plt.show() 

    fig_combined_partial_steps.savefig('/home/vijay/Rutgers/course_work/520/Reports/project_2_plots/Plot2_combined_information_setting.png') 

    ## All Plot
    
    fig_all = plt.figure(figsize = (40,10), dpi=80) # Decrease dpi to get higher resolution
    
    # creating the bar plot
    plt.bar(Agent_names, Catch_rates, color ='green',
            width = 0.2)
    plt.bar(Agent_names, Death_rates, color ='maroon',
            width = 0.4)
    plt.bar(Agent_names, Time_Out_rates, color ='yellow',
            width = 0.5)
            
    
    plt.xlabel("Agents")
    plt.ylabel("Success percentage")
    plt.title("Comparision of Success rates of different Agents:")
    #plt.show() 
    fig_all.savefig('/home/vijay/Rutgers/course_work/520/Reports/project_2_plots/Plot1_all.png')


    ## MISC plots

    figs = plt.figure(figsize = (10, 7)) # Decrease dpi to get higher resolution
    
    plt.xlabel("Agents")
    plt.ylabel("Percentage of Runs Agent Catches Prey")
    plt.title("Agent Catches:")
    plt.bar(Agent_names, Catch_rates, color ='green')
    plt.tight_layout()
    plt.xticks(rotation = 30)
    #plt.show() 
    figs.savefig('/home/vijay/Rutgers/course_work/520/Reports/project_2_plots/Success_Plot.png')

    figs = plt.figure(figsize = (10, 7))

    plt.xlabel("Agents")
    plt.ylabel("Percentage of Runs Agent Dies")
    plt.title("Agent Deaths:")
    plt.bar(Agent_names, Death_rates, color ='maroon')
    plt.tight_layout()
    plt.xticks(rotation = 30)
    #plt.show() 
    figs.savefig('/home/vijay/Rutgers/course_work/520/Reports/project_2_plots/Failure_Plot.png')

    figs = plt.figure(figsize = (10, 7))

    plt.xlabel("Agents")
    plt.ylabel("Average Steps taken by Agent")
    plt.title("Steps:")
    plt.bar(Agent_names, Steps_rates, color ='gold')
    plt.tight_layout()
    plt.xticks(rotation = 30)
    #plt.show() 
    figs.savefig('/home/vijay/Rutgers/course_work/520/Reports/project_2_plots/Avg_steps_plot.png')

    figs = plt.figure(figsize = (10, 7))

    plt.xlabel("Agents")
    plt.ylabel("Percentage of Steps Certain of Prey Position (and Correct)")
    plt.title("Percentage:")
    plt.bar(Prey_certain_agents, Prey_certain, color ='purple')
    plt.tight_layout()
    plt.xticks(rotation = 30)
    #plt.show() 
    figs.savefig('/home/vijay/Rutgers/course_work/520/Reports/project_2_plots/Prey_certainity_Plot.png')

    figs = plt.figure(figsize = (10, 7))

    plt.xlabel("Agents")
    plt.ylabel("Percentage of Steps Certain of Predator Position (and Correct)")
    plt.title("Percentage:")
    plt.bar(Predator_certain_agents, Predator_certain, color ='pink')
    plt.tight_layout()
    plt.xticks(rotation = 30)
    #plt.show() 
    figs.savefig('/home/vijay/Rutgers/course_work/520/Reports/project_2_plots/Predator_certainity_plot.png')



if __name__ == '__main__':
    main()