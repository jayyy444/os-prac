# MEMORY ALLOCATION ALGORITHMS

# INPUT
n = int(input("Enter number of processes: "))

processes = list(map(int, input("Enter process sizes: ").split()))

m = int(input("Enter number of blocks: "))

blocks = list(map(int, input("Enter block sizes: ").split()))





# BEST FIT
def best_fit():

    memory = blocks.copy()

    allocation = [-1] * n

    for i in range(n):

        best = -1

        for j in range(m):

            if memory[j] >= processes[i]:

                if best == -1 or memory[j] < memory[best]:

                    best = j

        if best != -1:

            allocation[i] = best

            memory[best] -= processes[i]

    print("\n===== BEST FIT =====")

    print("Process\tSize\tBlock")

    for i in range(n):

        if allocation[i] != -1:

            print(f"P{i+1}\t{processes[i]}\tB{allocation[i]+1}")

        else:

            print(f"P{i+1}\t{processes[i]}\tNot Allocated")


# WORST FIT
def worst_fit():

    memory = blocks.copy()

    allocation = [-1] * n

    for i in range(n):

        worst = -1

        for j in range(m):

            if memory[j] >= processes[i]:

                if worst == -1 or memory[j] > memory[worst]:

                    worst = j

        if worst != -1:

            allocation[i] = worst

            memory[worst] -= processes[i]

    print("\n===== WORST FIT =====")

    print("Process\tSize\tBlock")

    for i in range(n):

        if allocation[i] != -1:

            print(f"P{i+1}\t{processes[i]}\tB{allocation[i]+1}")

        else:

            print(f"P{i+1}\t{processes[i]}\tNot Allocated")


# FUNCTION CALLS


best_fit()

worst_fit()