# PRIORITY AND ROUND ROBIN SCHEDULING


def input_processes(n, priority=False):

    processes = []

    for i in range(n):

        at = int(input(f"Arrival Time P{i+1}: "))
        bt = int(input(f"Burst Time P{i+1}: "))

        if priority:

            pr = int(input(f"Priority P{i+1}: "))

            processes.append({
                "pid": i+1,
                "at": at,
                "bt": bt,
                "pr": pr
            })

        else:

            processes.append({
                "pid": i+1,
                "at": at,
                "bt": bt
            })

    return processes



def gantt(chart):

    print("\nGantt Chart:\n")

    for p in chart:
        print(f"| P{p} ", end="")

    print("|")



def calculate(processes, priority=False):

    total_wt = 0
    total_tat = 0

    if priority:
        print("\nPID\tAT\tBT\tPR\tWT\tTAT")
    else:
        print("\nPID\tAT\tBT\tWT\tTAT")

    for p in processes:

        wt = p["ct"] - p["at"] - p["bt"]

        tat = p["ct"] - p["at"]

        total_wt += wt
        total_tat += tat

        if priority:

            print(f"P{p['pid']}\t{p['at']}\t{p['bt']}\t{p['pr']}\t{wt}\t{tat}")

        else:

            print(f"P{p['pid']}\t{p['at']}\t{p['bt']}\t{wt}\t{tat}")

    print("\nAverage WT =", total_wt / len(processes))

    print("Average TAT =", total_tat / len(processes))


def priority_non():

    n = int(input("Enter number of processes: "))

    p = input_processes(n, True)

    time = 0
    done = 0

    chart = []

    while done < n:

        ready = [x for x in p if x["at"] <= time and "ct" not in x]

        if ready:

            proc = min(ready, key=lambda x: x["pr"])

            chart.append(proc["pid"])

            time += proc["bt"]

            proc["ct"] = time

            done += 1

        else:
            time += 1

    gantt(chart)

    calculate(p, True)



def priority_pre():

    n = int(input("Enter number of processes: "))

    p = input_processes(n, True)

    for x in p:
        x["rt"] = x["bt"]

    time = 0
    done = 0

    chart = []

    while done < n:

        ready = [x for x in p if x["at"] <= time and x["rt"] > 0]

        if ready:

            proc = min(ready, key=lambda x: x["pr"])

            chart.append(proc["pid"])

            proc["rt"] -= 1

            time += 1

            if proc["rt"] == 0:

                proc["ct"] = time

                done += 1

        else:
            time += 1

    gantt(chart)

    calculate(p, True)


def round_robin():

    n = int(input("Enter number of processes: "))

    tq = int(input("Enter time quantum: "))

    p = input_processes(n)

    for x in p:
        x["rt"] = x["bt"]

    time = 0

    queue = []

    chart = []

    while True:

        for proc in p:

            if proc["at"] == time:
                queue.append(proc)

        if queue:

            proc = queue.pop(0)

            chart.append(proc["pid"])

            execute = min(tq, proc["rt"])

            proc["rt"] -= execute

            time += execute

            for newp in p:

                if newp["at"] > time - execute and newp["at"] <= time:
                    queue.append(newp)

            if proc["rt"] > 0:
                queue.append(proc)

            else:
                proc["ct"] = time

        else:
            time += 1

        if all(x["rt"] == 0 for x in p):
            break

    gantt(chart)

    calculate(p)


while True:

    print("\n===== CPU SCHEDULING MENU =====")

    print("1. Priority Non Preemptive")

    print("2. Priority Preemptive")

    print("3. Round Robin")

    print("4. Exit")

    ch = int(input("Enter your choice: "))

    if ch == 1:

        priority_non()

    elif ch == 2:

        priority_pre()

    elif ch == 3:

        round_robin()

    elif ch == 4:

        print("\nExiting Program...")

        break

    else:

        print("\nInvalid Choice")
