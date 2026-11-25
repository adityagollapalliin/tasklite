"""Command-line interface for tasklite."""

from __future__ import annotations

import argparse

from tasklite.store import TaskStore


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="tasklite", description="Tiny to-do list manager")
    sub = parser.add_subparsers(dest="command", required=True)

    add = sub.add_parser("add", help="Add a task")
    add.add_argument("title")
    add.add_argument("--due", help="Due date, YYYY-MM-DD")

    sub.add_parser("list", help="List tasks")

    done = sub.add_parser("done", help="Mark a task as done")
    done.add_argument("id", type=int)

    remove = sub.add_parser("remove", help="Remove a task")
    remove.add_argument("id", type=int)
    return parser


def format_task(task) -> str:
    mark = "x" if task.done else " "
    due = f" (due {task.due})" if task.due else ""
    return f"[{mark}] {task.id}. {task.title}{due}"


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    store = TaskStore()

    if args.command == "add":
        task = store.add(args.title, due=args.due)
        print(f"Added task {task.id}: {task.title}")
    elif args.command == "list":
        for task in store.tasks:
            print(format_task(task))
    elif args.command == "done":
        task = store.complete(args.id)
        print(f"Completed task {task.id}")
    elif args.command == "remove":
        task = store.remove(args.id)
        print(f"Removed task {task.id}")
    return 0
