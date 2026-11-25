"""Load and save tasks to a JSON file."""

from __future__ import annotations

import json
import os
from dataclasses import asdict, dataclass, field
from pathlib import Path


def default_path() -> Path:
    return Path(os.environ.get("TASKLITE_FILE", "tasks.json"))


@dataclass
class Task:
    id: int
    title: str
    done: bool = False
    due: str | None = None
    tags: list[str] = field(default_factory=list)


class TaskStore:
    def __init__(self, path: Path | None = None) -> None:
        self.path = path or default_path()
        self.tasks: list[Task] = []
        self.load()

    def load(self) -> None:
        if not self.path.exists():
            self.tasks = []
            return
        raw = json.loads(self.path.read_text())
        self.tasks = [Task(**item) for item in raw]

    def save(self) -> None:
        self.path.write_text(json.dumps([asdict(t) for t in self.tasks], indent=2))

    def next_id(self) -> int:
        # Known bug (see issues): ids are reused after a task is removed.
        return len(self.tasks) + 1

    def add(self, title: str, due: str | None = None) -> Task:
        task = Task(id=self.next_id(), title=title, due=due)
        self.tasks.append(task)
        self.save()
        return task

    def get(self, task_id: int) -> Task:
        for task in self.tasks:
            if task.id == task_id:
                return task
        raise KeyError(f"No task with id {task_id}")

    def complete(self, task_id: int) -> Task:
        task = self.get(task_id)
        task.done = True
        self.save()
        return task

    def remove(self, task_id: int) -> Task:
        task = self.get(task_id)
        self.tasks.remove(task)
        self.save()
        return task
