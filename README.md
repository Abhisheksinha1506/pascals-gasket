# 📐 Pascal's Gasket (Sierpiński Triangle)

> "Building a fractal pyramid one row at a time from a single drop of math."

### 📢 Latest Status
<!-- LATEST_STATUS_START -->
> The Sierpiński pyramid has grown to Row 115. This new layer adds 16 mathematical blocks to the gasket. The fractal symmetry is maintaining perfect proportion as the triangle descends.
<!-- LATEST_STATUS_END -->

### 📖 The Analogy
Imagine stacking cannonballs in a triangle. In the very top row, you have one. In the next row, two... and so on. This is Pascal's Triangle, a famous mountain of numbers where each number is the sum of the two above it.

Now, imagine a rule: if a number is **odd**, we color it in with a block (█). If it's **even**, we leave it blank. As this mountain grows, a beautiful fractal pattern called the Sierpiński Triangle emerges—a large triangle made of smaller triangles, with infinite holes inside.

### 🌱 How it Evolves
The triangle is being built row-by-row:
1. **Adding the Rows**: The script calculates the next row of the mathematical mountain.
2. **Filtering for Odds**: It converts the numbers into █ blocks or spaces.
3. **Building the Gasket**: The row is centered and appended to [triangle.md](triangle.md).
4. **Saving History**: The latest row's data is stored in [state.json](state.json).

**The pyramid grows on its own, approaching infinite complexity.**

### 🔍 Quick Links
- [The Triangle Gasket](triangle.md) — View the growing fractal pattern.
- [Current Row Data](state.json) — The raw numbers of the latest generation.
- [The Architect](evolve.py) — The script that builds the mountain.
