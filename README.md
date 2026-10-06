# To-Do List (Python)

DecodeLabs Python Programming - Project 1 (Batch 2026).

A command-line to-do list that lets you add, view, complete and delete tasks.
Tasks are stored in a list of dictionaries and saved to `tasks.json`, so they
survive after the program closes.

## Features
- Add tasks (`list.append`)
- View tasks with numbering (`enumerate`)
- Mark tasks as done / delete tasks
- Saves to JSON (persistence)
- Data logic (model) separated from the user interface (view)

## Run
Requires Python 3.8+.

```bash
python todo.py
```

## Example
```
=== TO-DO LIST ===
1. Add a task
2. View tasks
3. Mark a task as done
4. Delete a task
5. Exit

Your tasks:
  1. [x] Finish Python assignment
  2. [ ] Buy milk
```

## Concepts practiced
Lists, dictionaries, loops, functions, JSON file handling, `if __name__ == "__main__"`.
