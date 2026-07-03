SIZE = 5

queue = [None, None, None, None, None]

front = -1
rear = -1


def enqueue():
    global front, rear

    if (rear + 1) % SIZE == front:
        print("Queue is Full")
        return

    vehicle = input("Enter Vehicle Number: ")

    if front == -1:
        front = 0
        rear = 0
    else:
        rear = (rear + 1) % SIZE

    queue[rear] = vehicle
    print("Vehicle Added Successfully")


def dequeue():
    global front, rear

    if front == -1:
        print("Queue is Empty")
        return

    print("Vehicle Removed:", queue[front])

    if front == rear:
        front = -1
        rear = -1
    else:
        front = (front + 1) % SIZE


def display():
    if front == -1:
        print("Queue is Empty")
        return

    print("Vehicles in Queue:")

    i = front

    while True:
        print(queue[i])

        if i == rear:
            break

        i = (i + 1) % SIZE


while True:
    print("\n----- Parking Queue Menu -----")
    print("1. Enqueue Vehicle")
    print("2. Dequeue Vehicle")
    print("3. Display Queue")
    print("4. Exit")

    choice = int(input("Enter Your Choice: "))

    if choice == 1:
        enqueue()

    elif choice == 2:
        dequeue()

    elif choice == 3:
        display()

    elif choice == 4:
        print("Program Ended")
        break

    else:
        print("Invalid Choice")