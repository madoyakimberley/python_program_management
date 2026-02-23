# Import required libraries for UI and time validation
from rich.console import Console
from rich.panel import Panel
from rich.theme import Theme
from datetime import datetime
import argparse
import sys

# Import models and helper functions
from models.user import User
from utils.helpers import load_users, save_users

# Define custom theme for styled terminal output
custom_theme = Theme({
    "primary": "bold hot_pink",
    "secondary": "medium_purple",
    "success": "bold bright_magenta",
    "error": "bold deep_pink4",
    "warning": "bold plum4",
    "menu": "bold orchid1",
})

# Initialize console with theme
console = Console(theme=custom_theme)

# Load users from persistent storage at startup
users = load_users()


# Function to display application menu
def show_menu():
    console.print(
        Panel.fit(
            "[menu]PROJECT MANAGEMENT SYSTEM[/menu]\n\n"
            "[primary]Enter The numbers to select an Option[/primary]\n\n"
            "[secondary]1.[/secondary] Add User\n"
            "[secondary]2.[/secondary] List Users\n"
            "[secondary]3.[/secondary] Add Project\n"
            "[secondary]4.[/secondary] List Projects\n"
            "[secondary]5.[/secondary] Add Task\n"
            "[secondary]6.[/secondary] Complete Task\n"
            "[secondary]7.[/secondary] Delete User\n"
            "[secondary]8.[/secondary] Delete Project\n"
            "[secondary]9.[/secondary] Delete Task\n"
            "[secondary]10.[/secondary] Exit\n",
            title="[primary]Welcome[/primary]",
            border_style="secondary"
        )
    )


# Main application loop
def main():

    # Show menu once at program start
    show_menu()

    # Allow modification of global users list
    global users

    # Infinite loop to keep program running until user exits
    while True:

        # Get user menu selection
        choice = input("\nSelect option: ").strip()

        # Option 1 -> Add User
        if choice == "1":
            name = input("Name: ")
            email = input("Email: ")

            # Prevent duplicate users
            if any(u.email == email for u in users):
                console.print("[error]User already exists.[/error]")
            else:
                users.append(User(name, email))
                save_users(users)
                console.print("[success]User created successfully.[/success]")

        # Option 2 → List Users
        elif choice == "2":
            if not users:
                console.print("[warning]No users found.[/warning]")
            else:
                for user in users:
                    console.print(f"[primary]{user}[/primary]")

        # Option 3 -> Add Project to a User
        elif choice == "3":
            email = input("User Email: ")
            user = next((u for u in users if u.email == email), None)

            # Validate user existence
            if not user:
                console.print("[error]User not found.[/error]")
                continue

            title = input("Project Title: ")
            description = input("Description: ")
            due_date = input("Due Date (YYYY-MM-DD): ")
            github_repo = input("GitHub Repo (optional): ")

            # Validate date format
            try:
                datetime.strptime(due_date, "%Y-%m-%d")
            except ValueError:
                console.print("[error]Invalid date format.[/error]")
                continue

            # Add project and save changes
            user.add_project(title, description, due_date, github_repo or None)
            save_users(users)

            console.print("[success]Project created successfully.[/success]")

        # Option 4 -> List Projects and Tasks
        elif choice == "4":
            email = input("User Email: ")
            user = next((u for u in users if u.email == email), None)

            if not user:
                console.print("[error]User not found.[/error]")
                continue

            if not user.projects:
                console.print("[warning]No projects found.[/warning]")
                continue

            for project in user.projects:
                console.print(f"\n[primary]{project}[/primary]")

                if not project.tasks:
                    console.print("   [warning]No tasks yet.[/warning]")
                else:
                    for task in project.tasks:

                        # Set style based on task status
                        status_style = "success" if task.status == "completed" else "warning"

                        console.print(
                            f"   [secondary]ID:[/secondary] {task.id} | "
                            f"{task.title} | "
                            f"Assigned to: {task.assigned_to or 'N/A'} | "
                            f"[{status_style}]{task.status}[/{status_style}]"
                        )

        # Option 5 -> Add Task to Project
        elif choice == "5":
            email = input("User Email: ")
            user = next((u for u in users if u.email == email), None)

            if not user:
                console.print("[error]User not found.[/error]")
                continue

            project_title = input("Project Title: ")
            project = user.get_project_by_title(project_title)

            if not project:
                console.print("[error]Project not found.[/error]")
                continue

            task_title = input("Task Title: ")
            assigned_to = input("Assigned To (optional): ")

            project.add_task(task_title, assigned_to or None)
            save_users(users)

            console.print("[success]Task added successfully.[/success]")

        # Option 6 -> Complete Task
        elif choice == "6":
            email = input("User Email: ")
            user = next((u for u in users if u.email == email), None)

            if not user:
                console.print("[error]User not found.[/error]")
                continue

            project_title = input("Project Title: ")
            project = user.get_project_by_title(project_title)

            if not project:
                console.print("[error]Project not found.[/error]")
                continue

            try:
                task_id = int(input("Task ID: "))
            except ValueError:
                console.print("[error]Invalid Task ID.[/error]")
                continue

            task = project.get_task_by_id(task_id)

            if not task:
                console.print("[error]Task not found.[/error]")
                continue

            task.mark_complete()
            save_users(users)

            console.print("[success]Task marked as completed.[/success]")

        # Option 7 -> Delete User
        elif choice == "7":
            email = input("User Email: ")
            users = [u for u in users if u.email != email]
            save_users(users)

            console.print("[success]User deleted if existed.[/success]")

        # Option 8 -> Delete Project
        elif choice == "8":
            email = input("User Email: ")
            user = next((u for u in users if u.email == email), None)

            if not user:
                console.print("[error]User not found.[/error]")
                continue

            title = input("Project Title: ")
            user.projects = [p for p in user.projects if p.title != title]
            save_users(users)

            console.print("[success]Project deleted if existed.[/success]")

        # Option 9 -> Delete Task
        elif choice == "9":
            email = input("User Email: ")
            user = next((u for u in users if u.email == email), None)

            if not user:
                console.print("[error]User not found.[/error]")
                continue

            project_title = input("Project Title: ")
            project = user.get_project_by_title(project_title)

            if not project:
                console.print("[error]Project not found.[/error]")
                continue

            try:
                task_id = int(input("Task ID: "))
            except ValueError:
                console.print("[error]Invalid Task ID.[/error]")
                continue

            project.tasks = [t for t in project.tasks if t.id != task_id]
            save_users(users)

            console.print("[success]Task deleted if existed.[/success]")

        # Option 10 -> Exit Program
        elif choice == "10":
            console.print("[primary]Exiting... Goodbye![/primary]")
            break

        # Invalid input handling
        else:
            console.print("[error]Invalid choice.[/error]")


# Run program only if executed directly
def create_parser():
    parser = argparse.ArgumentParser(
        description="Project Management CLI Tool"
    )

    subparsers = parser.add_subparsers(dest="command")

    # -------- Add User -------- #
    add_user = subparsers.add_parser("add-user")
    add_user.add_argument("--name", required=True)
    add_user.add_argument("--email", required=True)

    # -------- List Users -------- #
    subparsers.add_parser("list-users")

    # -------- Add Project -------- #
    add_project = subparsers.add_parser("add-project")
    add_project.add_argument("--email", required=True)
    add_project.add_argument("--title", required=True)
    add_project.add_argument("--description", required=True)
    add_project.add_argument("--due-date", required=True)
    add_project.add_argument("--github", required=False)

    return parser


def handle_cli(args):
    global users

    # ---- ADD USER ---- #
    if args.command == "add-user":
        if any(u.email == args.email for u in users):
            print("User already exists.")
        else:
            users.append(User(args.name, args.email))
            save_users(users)
            print("User added successfully.")

    # ---- LIST USERS ---- #
    elif args.command == "list-users":
        for user in users:
            print(user)

    # ---- ADD PROJECT ---- #
    elif args.command == "add-project":
        user = next((u for u in users if u.email == args.email), None)

        if not user:
            print("User not found.")
            return

        try:
            datetime.strptime(args.due_date, "%Y-%m-%d")
        except ValueError:
            print("Invalid date format.")
            return

        user.add_project(
            args.title,
            args.description,
            args.due_date,
            args.github
        )

        save_users(users)
        print("Project added successfully.")


def create_parser():
    parser = argparse.ArgumentParser(
        description="Project Management CLI Tool"
    )

    subparsers = parser.add_subparsers(dest="command")

    # ---- Add User ---- #
    add_user = subparsers.add_parser("add-user")
    add_user.add_argument("--name", required=True)
    add_user.add_argument("--email", required=True)

    # ---- List Users ---- #
    subparsers.add_parser("list-users")

    # ---- Add Project ---- #
    add_project = subparsers.add_parser("add-project")
    add_project.add_argument("--email", required=True)
    add_project.add_argument("--title", required=True)
    add_project.add_argument("--description", required=True)
    add_project.add_argument("--due-date", required=True)
    add_project.add_argument("--github", required=False)

    return parser


def handle_cli(args):
    global users

    if args.command == "add-user":
        if any(u.email == args.email for u in users):
            print("User already exists.")
        else:
            users.append(User(args.name, args.email))
            save_users(users)
            print("User added successfully.")

    elif args.command == "list-users":
        for user in users:
            print(user)

    elif args.command == "add-project":
        user = next((u for u in users if u.email == args.email), None)

        if not user:
            print("User not found.")
            return

        try:
            datetime.strptime(args.due_date, "%Y-%m-%d")
        except ValueError:
            print("Invalid date format.")
            return

        user.add_project(
            args.title,
            args.description,
            args.due_date,
            args.github
        )

        save_users(users)
        print("Project added successfully.")


def main():
    parser = create_parser()
    args = parser.parse_args()

    # If user passed a subcommand → run CLI mode
    if args.command:
        handle_cli(args)
        sys.exit()

    # Otherwise → run interactive mode
    show_menu()


if __name__ == "__main__":
    main()