import random

from django.core.management.base import BaseCommand
from api.models import Board, Label, List, Project, Task


class Command(BaseCommand):
    help = "Seeds the database with one project, its boards, lists, distinct tasks, and labels."

    def handle(self, *args, **kwargs):
        # Clear existing data
        Task.objects.all().delete()
        List.objects.all().delete()
        Board.objects.all().delete()
        Label.objects.all().delete()
        Project.objects.all().delete()

        # Create the project
        project = Project.objects.create(
            title="Nick Fryingpan's Warhammer Website",
            description="A comprehensive website showcasing Nick Fryingpan's Warhammer miniatures, tactics, and community interactions.",
        )

        # Define board names
        board_titles = ["Content Management",
                        "Design and Layout", "Community Features"]

        # Create labels for the project
        label_titles = ["Urgent", "Bug",
                        "Feature Request", "Research", "Enhancement"]
        labels = []
        for title in label_titles:
            label = Label.objects.create(
                title=title,
                colour=f"#{random.randint(0, 0xFFFFFF):06x}",
                project=project,
            )
            labels.append(label)

        # Define realistic tasks for each list
        list_tasks = {
            "Backlog": [
                "Draft initial content plan",
                "Identify core audience for Warhammer community",
                "Research popular Warhammer topics",
                "List required website features",
                "Prepare a timeline for website launch",
            ],
            "To Do": [
                "Write lore article on Space Marines",
                "Compile top 10 miniature painting tips",
                "Set up a gallery for Warhammer miniatures",
                "Create a poll for favorite Warhammer factions",
                "Add a feedback form for users",
            ],
            "In Progress": [
                "Optimize homepage layout for mobile",
                "Add search functionality to the website",
                "Edit and upload battle report video",
                "Fix broken links in navigation menu",
                "Implement category filtering for blog posts",
            ],
            "Done": [
                "Purchase domain and hosting",
                "Set up basic website framework",
                "Upload Warhammer faction logos",
                "Publish first blog post",
                "Configure SSL for secure browsing",
            ],
        }

        # Create boards, lists, and tasks
        for board_title in board_titles:
            board = Board.objects.create(project=project, title=board_title)

            # Create lists and their tasks
            for position, (list_title, tasks) in enumerate(list_tasks.items(), start=1):
                task_list = List.objects.create(
                    board=board,
                    title=f"{list_title} ({board_title})",
                    position=position,
                )

                # Create tasks for the list
                for task_title in tasks:
                    task_priority = random.choice(
                        [Task.Priority.HIGH, Task.Priority.MEDIUM, Task.Priority.LOW])
                    task_story_points = random.choice([5, 10, 15, 20])

                    # Create the task
                    task = Task.objects.create(
                        list=task_list,
                        title=f"{task_title}",
                        description=f"{task_title} is part of the {list_title} list for {board_title}.",
                        priority=task_priority,
                        story_points=task_story_points,
                    )

                    # Assign random labels to the task
                    assigned_labels = random.sample(
                        labels, k=random.randint(1, 3))
                    task.labels.add(*assigned_labels)

        self.stdout.write(self.style.SUCCESS(
            "Database seeded with Nick Fryingpan's Warhammer Website, distinct tasks, and labels."))
