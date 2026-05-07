# Producer Consumer Problem

buffer = []

size = int(input("Enter buffer size: "))
item = 0

while True:

    print("\n1.PRODUCER")
    print("2.CONSUMER")
    print("3.EXIT")

    n = int(input("\nENTER YOUR CHOICE "))

    # PRODUCER
    if n == 1:

        if len(buffer) == size:
            print("BUFFER IS FULL")

        else:
            item += 1
            buffer.append(item)
            print("producer produces the item", item)

    # CONSUMER
    elif n == 2:

        if len(buffer) == 0:
            print("BUFFER IS EMPTY")

        else:
            item = buffer.pop()
            print("consumer consumes item", item)

    # EXIT
    elif n == 3:

        print("\nEXIT...\n")
        break

    else:
        print("Invalid Choice")