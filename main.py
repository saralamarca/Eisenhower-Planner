import os
from eisenhower_planner import Task, EisenhowerPlanner
from eisenhower_gui import EisenhowerGUI


if __name__ == "__main__":
    # Initialize and run the GUI
    # EisenhowerGUI().run()
    # Create an instance of EisenhowerPlanner
    eisenhower_matrix = EisenhowerPlanner()
    print("*** Welcome to the Eisenhower Matrix Planner ***\n")

    # Prompt user to load an existing matrix
    if eisenhower_matrix.get_input("Do you want to load an existing matrix? (yes/no): "):
        load_path = input("Enter the full path to load your matrix (e.g., /path/to/eisenhower_matrix.csv): ")
        # Load matrix from specified directory
        eisenhower_matrix.load_matrix(os.path.dirname(load_path))

    # Main loop to display menu and handle user interaction
    while True:
        print("\nMenu:")
        print("1. Add Task")
        print("2. Edit Task")
        print("3. Delete Task")
        print("4. Save and Exit")
        print("5. Exit without Saving")
        # Get user's menu choice
        choice = input("Choose an option: ")  

        # Option to add a new task
        if choice == '1':
            task_name = input("Enter task name: ")
            # Allow quitting from this menu point
            if task_name.lower() == 'quit':
                break
            # Determine urgency of the task
            urgent = eisenhower_matrix.get_input("Is the task urgent? (yes/no): ")
            # Determine importance of the task
            important = eisenhower_matrix.get_input("Is the task important? (yes/no): ")
            # Create a new Task instance
            task = Task(task_name, urgent, important)
            # Add the new task to the matrix
            eisenhower_matrix.add_task(task)

        # Option to edit an existing task
        elif choice == '2':
            eisenhower_matrix.edit_task()

        # Option to delete an existing task
        elif choice == '3':  
            eisenhower_matrix.delete_task()

        # Option to save and exit
        elif choice == '4':
            save_path = input("Enter the full path to save your matrix (e.g., /path/to/eisenhower_matrix.csv): ")
            # Save the matrix to the specified directory
            eisenhower_matrix.save_matrix(os.path.dirname(save_path))
            break

        # Option to exit without saving
        elif choice == '5':
            break

    # Display the current state of the Eisenhower Matrix after exiting the menu
    print("\nEisenhower Matrix:\n")
    eisenhower_matrix.display_matrix()
