"""
Tool to help ju priorotize your tasks based on the Eisenhower Matrix method.

Functionalities:
- Add tasks with urgency and importance attributes.
- Categorize tasks into Do, Schedule, Delegate, Delete based on urgency and importance.
- Display categorized tasks within the Eisenhower Matrix.
- Interactive user input to continuously add tasks and assess their categories.

TODO: Add functionality to remove tasks from the matrix.
"""

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

    def display_matrix(self):
        """
        Prints out the tasks organized by category.
        """
        for category, tasks in self.matrix.items():
            print(f"{category.upper()}:")
            for task in tasks:
                print(f"- {task.name}")
            print()

    def get_input(self, prompt):
        """
        Get input from user ('yes' or 'no').
        
        Parameters:
            prompt (str): Question to answer.
        
        Returns:
            bool: True if 'yes', False if 'no'.
        """
        while True:
            try:
                return {"yes": True, "no": False}[input(prompt)]
            except KeyError:
                print("Please enter 'yes' or 'no'")



if __name__ == "__main__":
    eisenhower_matrix = EisenhowerPlanner()
    print("*** Welcome to the Eisenhower Planner ***\n")

    while True:
        print("\nEnter your task, (type 'quit' to exit):")
        task_name = input("Task: ")
        if task_name.lower() == 'quit':
            break

        urgent = eisenhower_matrix.get_input("Is the task urgent? (type 'yes' or 'no'): ")
        important = eisenhower_matrix.get_input("Is the task important? (type 'yes' or 'no'): ")

        task = Task(task_name, urgent, important)
        eisenhower_matrix.add_task(task)

    print("\nEisenhower Matrix:\n")
    eisenhower_matrix.display_matrix()