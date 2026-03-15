import sys
import json
import os

MEMORY_FILE = os.path.join(os.path.dirname(os.path.dirname(__file__)), "memory.json")

def load_memory():
    if not os.path.exists(MEMORY_FILE):
        return {"username": "", "goals": [], "value_of_time": 0}
    with open(MEMORY_FILE, 'r') as f:
        return json.load(f)

def save_memory(data):
    with open(MEMORY_FILE, 'w') as f:
        json.dump(data, f, indent=4)

def update_username(name):
    data = load_memory()
    data["username"] = name
    save_memory(data)
    print(f"Username updated to: {name}")

def update_vot(val):
    data = load_memory()
    data["value_of_time"] = int(val)
    save_memory(data)
    print(f"Value of Time (V) updated to: {val:,} GP/hr")

def add_goal(goal):
    data = load_memory()
    data["goals"].append(goal)
    save_memory(data)
    print(f"Goal added: {goal}")

def remove_goal(index):
    data = load_memory()
    try:
        removed = data["goals"].pop(index)
        save_memory(data)
        print(f"Goal removed: {removed}")
    except IndexError:
        print("Invalid goal index.")

def show_memory():
    data = load_memory()
    print(f"Username: {data.get('username') or 'Not set'}")
    print(f"Value of Time (V): {data.get('value_of_time', 0):,} GP/hr")
    print("Current Goals:")
    if not data.get("goals"):
        print("  None")
    for i, goal in enumerate(data.get("goals", [])):
        print(f"  [{i}] {goal}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        show_memory()
    else:
        cmd = sys.argv[1]
        if cmd == "set-user":
            update_username(" ".join(sys.argv[2:]))
        elif cmd == "set-vot":
            update_vot(sys.argv[2])
        elif cmd == "add-goal":
            add_goal(" ".join(sys.argv[2:]))
        elif cmd == "remove-goal":
            remove_goal(int(sys.argv[2]))
        else:
            print("Usage: python manage_memory.py [set-user <name> | set-vot <value> | add-goal <goal> | remove-goal <index>]")
