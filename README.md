# Graph Implementation in Python

This repository contains the implementation of an undirected graph in Python.

## How to use

1. Clone this repository.
2. Run the `graph.py` file with Python.
3. Use the `add_edge()` method to add edges between nodes and `display()` to show the graph.

## Example

```python
g = Graph()
g.add_edge(1, 2)
g.add_edge(1, 3)
g.add_edge(2, 4)
g.add_edge(3, 4)

g.display()