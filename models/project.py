from .task import Task


class Project:
    id_counter = 1

    def __init__(self, title, description, due_date, github_repo=None):
        self.id = Project.id_counter
        Project.id_counter += 1

        self.title = title
        self.description = description
        self.due_date = due_date
        self.github_repo = github_repo
        self.tasks = []

    def add_task(self, title, assigned_to=None):
        task = Task(title, assigned_to)
        self.tasks.append(task)
        return task

    def get_task_by_id(self, task_id):
        for task in self.tasks:
            if task.id == task_id:
                return task
        return None

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "due_date": self.due_date,
            "github_repo": self.github_repo,
            "tasks": [task.to_dict() for task in self.tasks]
        }

    @classmethod
    def from_dict(cls, data):
        project = cls(
            data.get("title"),
            data.get("description"),
            data.get("due_date"),
            data.get("github_repo")
        )

        project.id = data.get("id", Project.id_counter)
        Project.id_counter = max(Project.id_counter, project.id + 1)

        project.tasks = [
            Task.from_dict(task_data)
            for task_data in data.get("tasks", [])
        ]

        return project