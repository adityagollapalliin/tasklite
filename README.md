# tasklite

A tiny command-line to-do list manager written in plain Python (no dependencies).

This repository is the **assigned project** for the OpenShell "CodeBuddy in a Box" demo:
an AI coding agent running inside an OpenShell sandbox is allowed to read *only this repo*
on GitHub, work on its open issues locally, and run its tests.

## Usage

```bash
python -m tasklite add "Buy milk"
python -m tasklite add "Write report" --due 2026-12-01
python -m tasklite list
python -m tasklite done 1
python -m tasklite remove 2
```

Tasks are stored in `tasks.json` in the current folder (override with `TASKLITE_FILE`).

## Development

```bash
python -m pytest -q
```

Open issues are good first tasks — see the Issues tab.
