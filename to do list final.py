

task = []


while True:
    print("\n--- To-Do List Menu ---")
    print("1. Create (Add a new task)")
    print("2. Update (Mark complete or change a task)")
    print("3. Track (View all tasks)")
    print("4. Exit")

    try:
        choice = int(input("Enter your choice: "))
    except ValueError:
        print("Invalid input! Please enter a number.")
        continue

    match choice:
        case 1:  # CREATE
            new_task = input("Enter the new task: ")
            task.append(new_task)
            print(f"Task '{new_task}' added successfully.")

        case 2:  # UPDATE
            if not task:
                print("Your to-do list is empty. Nothing to update.")
                continue
            print("Your current to-do list:")
            for i, t in enumerate(task, start=1):
                print(f"{i}. {t}")

            try:
                index = int(input("Enter the task number to mark as completed or update: ")) - 1
                if index < 0 or index >= len(task):
                    print("Invalid task number.")
                    continue

                action = input("Type 'done' to mark as completed or 'edit' to change the task: ").lower()
                if action == "done":
                    completed = task.pop(index)
                    print(f"Task '{completed}' marked as completed and removed.")
                elif action == "edit":
                    new_text = input("Enter the new task description: ")
                    task[index] = new_text
                    print("Task updated successfully.")
                else:
                    print("Invalid action.")

            except ValueError:
                print("Invalid number entered.")

        case 3:  # TRACK
            if not task:
                print("Your to-do list is empty.")
            else:
                print("Your current to-do list:")
                for i, t in enumerate(task, start=1):
                    print(f"{i}. {t}")

        case 4:  # EXIT
            print("Exiting... Goodbye!")
            break

        case _:  # INVALID CHOICE
            print("Invalid choice. Please try again.")



