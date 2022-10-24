import agent_1

def main():
    total = 100
    caught = 0
    died = 0
    time_out = 0
    for i in range(total):
        print(f"{i} ", end="", flush=True)
        test_agent_1 = agent_1.Agent_1()
        result = test_agent_1.move()
        if result == 1:
            caught += 1
        elif result == 0:
            died += 1
        elif result == -1:
            time_out +=1

    print(f"\nCaught (including timeout): {round((caught/total) * 100, 3)}% | Died (including timeout): {round((died/total) * 100, 3)}% | Timed Out %: {round((time_out/total) * 100, 3)}%")
    print(f"Caught (excluding timeout): {round((caught/(total-time_out)) * 100, 3)}% | Died (exlcuding) timeout): {round((died/(total-time_out) * 100),3)}%")

if __name__ == '__main__':
    main()