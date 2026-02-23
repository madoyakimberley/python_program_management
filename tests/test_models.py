# ==============================
# Pytest for Project Management
# ==============================

import pytest
from models.user import User
from models.project import Project
from models.task import Task



def test_user_creation():
    user = User("Kim", "kim@gmail.com")

    assert user.name == "Kim"
    assert user.email == "kim@gmail.com"
    assert user.projects == []


def test_add_project_to_user():
    user = User("Kim", "kim@gmail.com")

    project = user.add_project(
        "Backend",
        "API Development",
        "2025-12-01",
        "github.com/test"
    )

    assert project in user.projects
    assert project.title == "Backend"


def test_add_task_to_project():
    project = Project(
        "Backend",
        "API",
        "2025-12-01"
    )

    task = project.add_task("Build Auth", "Kim")

    assert task in project.tasks
    assert task.title == "Build Auth"


def test_get_task_by_id():
    project = Project(
        "Backend",
        "API",
        "2025-12-01"
    )

    task = project.add_task("Test Task", "Kim")

    found = project.get_task_by_id(task.id)

    assert found == task



def test_mark_task_complete():
    task = Task("Fix Bug", "Kim")

    assert task.status == "pending"

    task.mark_complete()

    assert task.status == "completed"