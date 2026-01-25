import os
import json
import datetime

def evolve():
    base_dir = os.path.dirname(__file__)
    state_path = os.path.join(base_dir, 'state.json')
    triangle_path = os.path.join(base_dir, 'triangle.md')

    with open(state_path, 'r') as f:
        state = json.load(f)

    current_row = state["row"]
    
    # Compute next row of Pascal's triangle mod 2
    # Row n+1 is [1] + [row[i] + row[i+1] mod 2 for i in range] + [1]
    new_row = [1]
    for i in range(len(current_row) - 1):
        new_row.append((current_row[i] + current_row[i+1]) % 2)
    new_row.append(1)

    # ASCII representation
    # Center the row for better visual gasket
    # Using a fixed width or just appending
    width = 121
    ascii_row = "".join(['█' if x else ' ' for x in current_row])
    padding = (width - len(ascii_row)) // 2
    centered_row = (" " * padding) + ascii_row + (" " * padding)

    date_str = datetime.date.today().isoformat()
    
    with open(triangle_path, 'a') as f:
        f.write(f"| {state['iteration']} | `{centered_row}` |\n")

    # Update state
    state["row"] = new_row
    state["iteration"] += 1
    
    with open(state_path, 'w') as f:
        json.dump(state, f, indent=4)

    # Generate human summary
    blocks = current_row.count(1)
    summary = f"The Sierpiński pyramid has grown to Row {state['iteration']}. "
    summary += f"This new layer adds {blocks} mathematical blocks to the gasket. "
    summary += "The fractal symmetry is maintaining perfect proportion as the triangle descends."

    with open(os.path.join(base_dir, 'summary.txt'), 'w') as f:
        f.write(summary)

if __name__ == "__main__":
    evolve()
