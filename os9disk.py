# Disk Scheduling Algorithms - Final Version

def fcfs(requests, head):
    seek_sequence = [head] + requests + [199]
    seek_time = 0

    for i in range(len(seek_sequence) - 1):
        seek_time += abs(seek_sequence[i+1] - seek_sequence[i])

    return seek_sequence, seek_time


def sstf(requests, head):
    req = requests.copy()
    seek_sequence = [head]
    seek_time = 0
    current = head

    while req:
        closest = min(req, key=lambda x: abs(x - current))
        seek_time += abs(current - closest)
        current = closest
        seek_sequence.append(current)
        req.remove(closest)

    # move to 199
    seek_time += abs(current - 199)
    current = 199
    seek_sequence.append(current)

    return seek_sequence, seek_time


def scan(requests, head, disk_size=199):
    left = [r for r in requests if r < head]
    right = [r for r in requests if r >= head]

    left.sort(reverse=True)
    right.sort()

    seek_sequence = [head]
    seek_time = 0
    current = head

    # move right
    for r in right:
        seek_time += abs(current - r)
        current = r
        seek_sequence.append(current)

    # go to 199
    if current != disk_size:
        seek_time += abs(current - disk_size)
        current = disk_size
        seek_sequence.append(current)

    # move left
    for r in left:
        seek_time += abs(current - r)
        current = r
        seek_sequence.append(current)

    # finally go to 0
    if current != 0:
        seek_time += abs(current - 0)
        current = 0
        seek_sequence.append(current)

    return seek_sequence, seek_time





# -------- MENU --------
while True:
    print("\n===== Disk Scheduling Algorithms =====")
    print("1. FCFS")
    print("2. SSTF")
    print("3. SCAN")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 5:
        print("Program Ended")
        break

    n = int(input("Enter total number of requests: "))

    # validation
    while True:
        requests = list(map(int, input("Enter request queue: ").split()))
        
        if len(requests) != n:
            print(f" Error: You entered {len(requests)} requests, expected {n}. Try again!")
        else:
            break

    head = int(input("Enter initial head position: "))

    if choice == 1:
        seq, time = fcfs(requests, head)
        print("\n--- FCFS ---")

    elif choice == 2:
        seq, time = sstf(requests, head)
        print("\n--- SSTF ---")

    elif choice == 3:
        seq, time = scan(requests, head)
        print("\n--- SCAN ---")


    else:
        print("Invalid Choice")
        continue

    print("Seek Sequence:", " -> ".join(map(str, seq)))
    print("Total Seek Time:", time)
