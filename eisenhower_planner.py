import csv
import os



class Task:
    """
    Defines task with labels for urgency and importance.
    
    Attributes:
        name (str): The name of the task.
        urgent (bool): True if the task is urgent, False otherwise.
        important (bool): True if the task is important, False otherwise.
    """
    def __init__(self, name, urgent, important):
        self.name = name
        self.urgent = urgent
        self.important = important


class EisenhowerPlanner:
    """
    A class for managing tasks based on urgency and importance.
    
    Attributes:
        matrix (dict of list of Task): A dictionary holding lists of tasks under 'do', 'schedule', 'delegate', 'delete'.
    """
    def __init__(self):
        self.matrix = {
            "do": [], # Urgent and important
            "schedule": [], # Important, not urgent
            "delegate": [], # Urgent, not important
            "delete": [] # Not urgent or important
        }

    def get_input(self, prompt):
        """
        Prompts the user for a yes/no input, ensuring valid response.

        Parameters:
            prompt (str): The question prompt to show to the user.

        Returns:
            bool: True if the user inputs 'yes', False if 'no'.
        """
        while True:
            response = input(prompt).strip().lower()
            if response in ["yes", "no"]:
                return response == "yes"
            print("Please enter 'yes' or 'no'")

    def add_task(self, task):
        """
        Add a task to the appropriate category based on urgency and importance.
        
        Parameters:
            task (Task): The task to add to the matrix.
        """
        if task.urgent and task.important:
            self.matrix["do"].append(task)
        elif not task.urgent and task.important:
            self.matrix["schedule"].append(task)
        elif task.urgent and not task.important:
            self.matrix["delegate"].append(task)
        elif not task.urgent and not task.important:
            self.matrix["delete"].append(task)

    def edit_task(self):
        """
        Interactive method to select and edit an existing task from a category.
        Allows user to change task name, urgency, and importance.
        """
        print("\nSelect a category to edit a task from:")
        for key in self.matrix:
            print(f"- {key}")

        category = input("Enter category: ").lower()
        if category in self.matrix and self.matrix[category]:
            print("\nTasks in this category:")
            for idx, task in enumerate(self.matrix[category]):
                print(f"{idx + 1}: {task.name}")

            while True:
                try:
                    task_number = int(input("\nEnter task number to edit: ")) - 1
                    if 0 <= task_number < len(self.matrix[category]):
                        task = self.matrix[category][task_number]
                        break
                    else:
                        print(f"Please enter a number between 1 and {len(self.matrix[category])}")
                except ValueError:
                    print("Invalid input. Please enter a valid integer.")

            print(f"Editing Task - {task.name}")
            task.name = input("Enter new task name: ")
            task.urgent = self.get_input("Is the task urgent? (yes/no): ")
            task.important = self.get_input("Is the task important? (yes/no): ")
            print("\nTask updated.")
        else:
            print("Invalid category or no tasks available.")

    def delete_task(self):
        """
        Interactive method to select and delete a task from a category.
        """
        print("\nSelect a category to delete a task from:")
        for key in self.matrix:
            print(f"- {key}")
        
        category = input("Enter category: ").lower()
        if category in self.matrix:
            print("\nTasks in this category:")
            for idx, task in enumerate(self.matrix[category]):
                print(f"{idx + 1}: {task.name}")
            
            task_number = int(input("\nEnter task number to delete: ")) - 1
            if 0 <= task_number < len(self.matrix[category]):
                del self.matrix[category][task_number]
                print("\nTask deleted successfully!")
            else:
                print("Invalid task number!")
        else:
            print("Invalid category!")

    def display_matrix(self):
        """
        Prints out the tasks organized by category.
        """
        for category, tasks in self.matrix.items():
            print(f"{category.upper()}:")
            for task in tasks:
                print(f"- {task.name}")
            print()

    def save_matrix(self, path, filename="eisenhower_matrix.csv"):
        """
        Saves the current Eisenhower Matrix to a CSV file.

        Parameters:
            path (str): The directory path where the file will be saved.
            filename (str): The name of the file to save the matrix to.
                            Default is 'eisenhower_matrix.csv'.
        """
        full_path = os.path.join(path, filename)
        try:
            with open(full_path, 'w', newline='') as f:
                writer = csv.writer(f)
                for category, tasks in self.matrix.items():
                    for task in tasks:
                        writer.writerow([category, task.name, task.urgent, task.important])
            print("Matrix saved.")
        except Exception as e:
            print(f"Failed to save: {e}")

    def load_matrix(self, path, filename="eisenhower_matrix.csv"):
        """
        Loads saved Eisenhower Matrix from CSV file.

        Parameters:
            path (str): The directory path where the file is located.
            filename (str): The name of the file from which to load the matrix.
                            Default is 'eisenhower_matrix.csv'.
        """
        full_path = os.path.join(path, filename)
        try:
            with open(full_path, newline='') as f:
                reader = csv.reader(f)
                self.matrix = {"do": [], "schedule": [], "delegate": [], "delete": []}
                for row in reader:
                    category, name, urgent, important = row
                    task = Task(name, urgent.lower() == 'true', important.lower() == 'true')
                    self.matrix[category]. append(task)
        except FileNotFoundError:
            print("File not found.")
