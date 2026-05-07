# Banker's Algorithm

n = int(input("Enter number of processes: "))
m = int(input("Enter number of resources: "))
start = int(input("Start process numbering from (0 or 1): "))

allocation = []
maximum = []

print("\nEnter Allocation Matrix:")
for i in range(n):
    row = list(map(int, input(f"P{start+i}: ").split()))
    allocation.append(row)

print("\nEnter Maximum Matrix:")
for i in range(n):
    row = list(map(int, input(f"P{start+i}: ").split()))
    maximum.append(row)

print("\nEnter Available Resources:")
available = list(map(int, input().split()))

# Calculate Need Matrix
need = []

for i in range(n):
    row = []
    for j in range(m):
        row.append(maximum[i][j] - allocation[i][j])
    need.append(row)

# Print Need Matrix
print("\nNeed Matrix:")
for i in range(n):
    print(f"P{start+i}:", need[i])

# Safety Algorithm
finish = [False] * n
safe = []

while len(safe) < n:

    allocated = False

    for i in range(n):

        if finish[i] == False:

            possible = True

            for j in range(m):

                if need[i][j] > available[j]:
                    possible = False
                    break

            if possible:

                for j in range(m):
                    available[j] += allocation[i][j]

                safe.append(i)
                finish[i] = True
                allocated = True

    if allocated == False:
        break

# Output
if len(safe) == n:

    print("\nSystem is in Safe State")

    print("Safe Sequence:")

    for i in safe:
        print(f"P{start+i}", end=" ")

else:
    print("\nSystem is NOT in Safe State")