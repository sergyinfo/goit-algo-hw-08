"""
Classical problem of combining cables
"""
import heapq

def min_cost_to_combine_cables(lengths: list) -> int:
    """
    Function to calculate the minimum cost to combine cables

    Parameters:
    lengths (list): List of integers representing the lengths of cables

    Returns:
    int: The minimum cost to combine cables

    Example:
    >>> min_cost_to_combine_cables([8, 4, 6, 12])
    """
    heapq.heapify(lengths)
    total_cost = 0

    # While there is more than one cable
    while len(lengths) > 1:
        # Remove the two smallest cables from the heap
        first = heapq.heappop(lengths)
        second = heapq.heappop(lengths)

        # Calculate the cost of combining the two cables
        cost = first + second
        total_cost += cost

        # Add the combined cable back to the heap
        heapq.heappush(lengths, cost)

    return total_cost

# Test the function
cable_lengths = [8, 4, 6, 12]
print(min_cost_to_combine_cables(cable_lengths))
