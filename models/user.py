from .project import Project


class User:
    id_counter = 1

    def __init__(self, name, email):
        self.id = User.id_counter
        User.id_counter += 1

        self.name = name
        self.email = email
        self.projects = []

    def add_project(self, title, description, due_date, github_repo=None):
        project = Project(title, description, due_date, github_repo)
        self.projects.append(project)
        return project

    def get_project_by_title(self, title):
        for project in self.projects:
            if project.title == title:
                return project
        return None

    def __str__(self):
        return f"User {self.id}: {self.name} ({self.email})"

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "email": self.email,
            "projects": [project.to_dict() for project in self.projects]
        }

    @classmethod
    def from_dict(cls, data):
        user = cls(data["name"], data["email"])
        user.id = data["id"]

        user.projects = [
            Project.from_dict(proj_data)
            for proj_data in data.get("projects", [])
        ]

        return user