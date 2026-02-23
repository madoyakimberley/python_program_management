class Task:
    id_counter = 1

    def __init__(self, title, assigned_to=None):
        self.id = Task.id_counter
        Task.id_counter += 1

        self.title = title
        self.status = "pending"
        self.assigned_to = assigned_to

    def mark_complete(self):
        self.status = "completed"

    def __str__(self):
        return f"[{self.id}] {self.title} - {self.status}"

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "status": self.status,
            "assigned_to": self.assigned_to
        }

    @classmethod
    def from_dict(cls, data):
        task = cls(data["title"], data.get("assigned_to"))
        task.id = data["id"]
        task.status = data["status"]
        return task