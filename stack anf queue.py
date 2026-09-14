queue = []
stack = []
pushed_shoe = []

CAPACITY = 10

prompt = ("""============ MAIN MENU ============
    1. Stack Operations (LIFO)
    2. Queue Operations (FIFO)
    0. Exit
    Enter choice: """)

message = True
while message:
    choice = int(input(prompt))
    if message == 1:
      menu = int(input("""--------- STACK MENU ---------
1. Push
2. Pop
3. Peek (Top)
4. Display Stack
5. Check if Empty
6. Check if Full
0. Back to Main Menu
Enter choice: """)) 
      if menu == 1:
        if len(pushed_shoe) >= CAPACITY:
            print("[Stack] Overflow! Stack is full.")

        else:
            push_message = int(input("Enter a Value to push: "))
            pushed_shoe += [push_message]

            print(f"[Stack] Pushed {push_message} onto the stack.")
            print(pushed_shoe)

      elif menu == 2:
        if len(pushed_shoe) == 0:
            print("[Stack] Underflow! Stack is empty.")
        else:
            popped_value = pushed_shoe[-1]
            del pushed_shoe[-1]
            print(f"[Stack] Popped Value: {popped_value}")
            print(pushed_shoe)
      elif menu == 3:

        if len(pushed_shoe) == 0:
            print("[Stack] Stack is empty.")
        else:
            print(f"[Stack] Top Value: {pushed_shoe[-1]}")

        print(pushed_shoe[-1])
      elif menu == 4:
        if len(pushed_shoe) == 0:
            print("[Stack] Stack is empty.")
        else:
            print("[Stack] Contents (Top to Bottom) ")
      elif menu == 5:
        if len(pushed_shoe) == 0:
            print("[Stack] Stack is EMPTY.")
        else:
            print("[Stack] Stack is NOT EMPTY.")
      elif menu == 6:

        if len(pushed_shoe) == CAPACITY:
            print("[Stack] Stack is FULL.")
        else:
            print("[Stack] Stack is NOT FULL.")
      elif menu == 0:
        break
      else:
        print("Invalid Stack choice.")
    elif message == 2:
        while True:
            menu = int(input("""--------- QUEUE MENU ---------
1. Enqueue
2. Dequeue
3. Peek (Front)
4. Display Queue
5. Check if Empty
6. Check if Full
0. Back to Main Menu
Enter choice: """))
        if menu == 1:
            if len(queue) >= CAPACITY:

            print("[Queue] Overflow! Queue is full.")

                else:
                    enqueue_value = int(input("Enter a Value to enqueue: "))

                    queue += [enqueue_value]

                    print(f"[Queue] Enqueued {enqueue_value} into the queue.")
                    print(queue)