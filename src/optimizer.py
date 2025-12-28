"""
Optimization utilities for PCB drill paths.
"""

def calculate_total_distance(points):
    """
    Calculate total drill path distance.

    This is a placeholder for future optimization algorithms
    such as greedy or TSP-based approaches.
    """
    if not points:
        return 0.0

    distance = 0.0
    for i in range(1, len(points)):
        dx = points[i].x - points[i-1].x
        dy = points[i].y - points[i-1].y
        distance += (dx**2 + dy**2) ** 0.5

    return distance
