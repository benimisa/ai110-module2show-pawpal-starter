from __future__ import annotations

from dataclasses import dataclass, field
from datetime import date, timedelta
from typing import List


@dataclass
class Task:
    """Represent a single pet care task."""

    description: str
    time: str
    frequency: str = "once"
    completed: bool = False
    priority: str = "medium"
    duration_minutes: int = 15
    parent_pet: "Pet | None" = field(default=None, repr=False, compare=False)
    due_date: date | None = None

    def mark_complete(self) -> None:
        """Mark the task complete and create a follow-up for recurring tasks."""
        self.completed = True
        if self.frequency in {"daily", "weekly"} and self.parent_pet is not None:
            self._create_next_occurrence()

    def _create_next_occurrence(self) -> None:
        """Create a new task for the next day or week when the task is recurring."""
        if self.parent_pet is None:
            return

        delta = timedelta(days=1 if self.frequency == "daily" else 7)
        next_due_date = (self.due_date or date.today()) + delta
        next_task = Task(
            description=self.description,
            time=self.time,
            frequency=self.frequency,
            priority=self.priority,
            duration_minutes=self.duration_minutes,
            parent_pet=self.parent_pet,
            due_date=next_due_date,
        )
        self.parent_pet.add_task(next_task)

    def to_dict(self) -> dict:
        """Return a dictionary view of the task."""
        return {
            "description": self.description,
            "time": self.time,
            "frequency": self.frequency,
            "completed": self.completed,
            "priority": self.priority,
            "duration_minutes": self.duration_minutes,
        }


@dataclass
class Pet:
    """Represent a pet and the tasks assigned to it."""

    name: str
    species: str
    tasks: List[Task] = field(default_factory=list)

    def add_task(self, task: Task) -> None:
        """Attach a task to this pet."""
        task.parent_pet = self
        self.tasks.append(task)

    def get_pending_tasks(self) -> List[Task]:
        """Return incomplete tasks for the pet."""
        return [task for task in self.tasks if not task.completed]


@dataclass
class Owner:
    """Represent a pet owner and the pets they manage."""

    name: str
    pets: List[Pet] = field(default_factory=list)

    def add_pet(self, pet: Pet) -> None:
        """Add a pet to the owner's care list."""
        self.pets.append(pet)

    def get_all_tasks(self) -> List[Task]:
        """Collect every task across all pets."""
        all_tasks: List[Task] = []
        for pet in self.pets:
            all_tasks.extend(pet.tasks)
        return all_tasks


class Scheduler:
    """Coordinate pet tasks and expose scheduling helpers."""

    def sort_by_time(self, tasks: List[Task]) -> List[Task]:
        """Sort tasks by their time string in chronological order."""
        return sorted(tasks, key=lambda task: tuple(int(part) for part in task.time.split(":")))

    def filter_tasks(self, tasks: List[Task], *, pet_name: str | None = None, completed: bool | None = None) -> List[Task]:
        """Filter tasks by pet name or completion status when provided."""
        filtered = list(tasks)
        if pet_name is not None:
            filtered = [task for task in filtered if (task.parent_pet and task.parent_pet.name == pet_name)]
        if completed is not None:
            filtered = [task for task in filtered if task.completed is completed]
        return filtered

    def detect_conflicts(self, tasks: List[Task]) -> List[str]:
        """Return warning messages for tasks that share the same time."""
        grouped: dict[str, List[str]] = {}
        for task in tasks:
            grouped.setdefault(task.time, []).append(task.description)

        conflicts: List[str] = []
        for time_value, descriptions in grouped.items():
            if len(descriptions) > 1:
                conflicts.append(f"{' and '.join(descriptions)} are both scheduled for {time_value}")
        return conflicts

    def build_daily_plan(self, owner: Owner) -> List[Task]:
        """Build a simple daily plan from the owner's pets and tasks."""
        tasks = owner.get_all_tasks()
        return self.sort_by_time([task for task in tasks if not task.completed])
