from pathlib import Path
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

    # Update README with latest status
    readme_path = os.path.join(base_dir, 'README.md')
    if os.path.exists(readme_path):
        with open(readme_path, 'r') as f:
            content = f.read()
        
        start_marker = "<!-- LATEST_STATUS_START -->"
        end_marker = "<!-- LATEST_STATUS_END -->"
        
        if start_marker in content and end_marker in content:
            parts = content.split(start_marker)
            prefix = parts[0] + start_marker
            suffix = end_marker + parts[1].split(end_marker)[1]
            new_content = f"{prefix}\n> {summary}\n{suffix}"
            
            with open(readme_path, 'w') as f:
                f.write(new_content)


def update_readme(summary):
    from pathlib import Path
    from datetime import datetime
    readme_path = Path("README.md")
    if not readme_path.exists(): return
    try:
        content = readme_path.read_text()
        start = "<!-- LATEST_STATUS_START -->"
        end = "<!-- LATEST_STATUS_END -->"
        if start not in content or end not in content: return
        parts = content.split(start)
        suffix_parts = parts[1].split(end)
        prefix = parts[0] + start
        suffix = end + suffix_parts[1]
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")
        new_inner = f"""
*{summary} ({timestamp})*
"""
        readme_path.write_text(prefix + new_inner + suffix)
    except Exception as e: print(f"⚠️ README Update Failed: {e}")
if __name__ == "__main__":
    evolve()
