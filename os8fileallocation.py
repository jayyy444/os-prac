

def sequential_allocation():

    print("\n--- Sequential Allocation ---")

    file_name = input("Enter file name: ")

    start = int(input("Enter starting block: "))

    length = int(input("Enter length of file: "))

    blocks = [start + i for i in range(length)]

    print("\nAllocated blocks are:\n")

    print(" -> ".join(map(str, blocks)))


def linked_allocation():

    print("\n--- Linked Allocation ---")

    file_name = input("Enter file name: ")

    start = int(input("Enter starting block: "))

    end = int(input("Enter ending block: "))

    blocks = [start]

    current = start

    while True:

        next_block = int(input(f"Next block after {current}: "))

        if next_block == -1:
            break

        blocks.append(next_block)

        current = next_block

    print("\nAllocated blocks are:\n")

    print(" -> ".join(map(str, blocks)))


def indexed_allocation():

    print("\n--- Indexed Allocation ---")

    file_name = input("Enter file name: ")

    index_block = int(input("Enter index block: "))

    end = int(input("Enter ending block: "))

    n = int(input("Enter number of blocks in index: "))

    blocks = []

    for i in range(n):

        block = int(input(f"Enter block {i + 1}: "))

        blocks.append(block)

    print("\nAll blocks are:\n")

    all_blocks = [index_block] + blocks

    print(" -> ".join(map(str, all_blocks)))


while True:

    print("\n===== File Allocation Strategies =====")

    print("1. Sequential")

    print("2. Linked")

    print("3. Indexed")

    print("4. Exit")

    choice = int(input("\nEnter your choice: "))

    if choice == 1:

        sequential_allocation()

    elif choice == 2:

        linked_allocation()

    elif choice == 3:

        indexed_allocation()

    elif choice == 4:

        print("\nExiting...")

        break

    else:

        print("\nInvalid choice! Try again.")

print("\n=== Code Execution Successful ===")