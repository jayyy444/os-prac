# PAGE REPLACEMENT ALGORITHMS

def print_result(history, status, faults, hits, pages):

    print("\nFrames Status:\n")

    frames = len(history[0])

    for i in range(frames - 1, -1, -1):
        print(f"F{i}", end="\t")

        for h in history:
            if h[i] == -1:
                print("-", end="\t")
            else:
                print(h[i], end="\t")
        print()

    print("St", end="\t")
    for s in status:
        print(s, end="\t")

    print("\n")
    print("Total Pages =", len(pages))
    print("Page Faults =", faults)
    print("Page Hits =", hits)

    ratio = (faults / len(pages)) * 100
    print("Fault Ratio = {:.2f}%".format(ratio))


# FIFO
def fifo():

    n = int(input("Enter number of pages: "))
    pages = list(map(int, input("Enter reference string: ").split()))
    frames = int(input("Enter number of frames: "))

    memory = [-1] * frames
    pointer = 0

    history = []
    status = []

    faults = 0
    hits = 0

    for page in pages:

        if page in memory:
            status.append("H")
            hits += 1

        else:
            memory[pointer] = page
            pointer = (pointer + 1) % frames

            status.append("F")
            faults += 1

        history.append(memory.copy())

    print("\n--- FIFO ---")
    print_result(history, status, faults, hits, pages)


# LRU
def lru():

    n = int(input("Enter number of pages: "))
    pages = list(map(int, input("Enter reference string: ").split()))
    frames = int(input("Enter number of frames: "))

    memory = []
    history = []
    status = []

    faults = 0
    hits = 0

    for page in pages:

        if page in memory:

            memory.remove(page)
            memory.append(page)

            hits += 1
            status.append("H")

        else:

            if len(memory) < frames:
                memory.append(page)
            else:
                memory.pop(0)
                memory.append(page)

            faults += 1
            status.append("F")

        temp = memory.copy()

        while len(temp) < frames:
            temp.insert(0, -1)

        history.append(temp)

    print("\n--- LRU ---")
    print_result(history, status, faults, hits, pages)


# OPTIMAL
def optimal():

    n = int(input("Enter number of pages: "))
    pages = list(map(int, input("Enter reference string: ").split()))
    frames = int(input("Enter number of frames: "))

    memory = []
    history = []
    status = []

    faults = 0
    hits = 0

    for i in range(len(pages)):

        page = pages[i]

        if page in memory:

            hits += 1
            status.append("H")

        else:

            if len(memory) < frames:
                memory.append(page)

            else:

                future = pages[i + 1:]
                index = []

                for m in memory:

                    if m in future:
                        index.append(future.index(m))
                    else:
                        index.append(999)

                replace = index.index(max(index))
                memory[replace] = page

            faults += 1
            status.append("F")

        temp = memory.copy()

        while len(temp) < frames:
            temp.insert(0, -1)

        history.append(temp)

    print("\n--- OPTIMAL ---")
    print_result(history, status, faults, hits, pages)


# MENU
while True:

    print("\n===== PAGE REPLACEMENT MENU =====")
    print("1. FIFO")
    print("2. LRU")
    print("3. OPTIMAL")
    print("4. Exit")

    ch = int(input("Enter choice: "))

    if ch == 1:
        fifo()

    elif ch == 2:
        lru()

    elif ch == 3:
        optimal()

    elif ch == 4:
        print("Exit")
        break

    else:
        print("Invalid Choice")