"""
Problem: Merge k sorted lists into one sorted list.
"""
import heapq

def merge_k_lists(lists: list) -> list:
    """
    Function to merge k sorted lists into one sorted list.

    Parameters:
    lists (list): List of sorted lists

    Returns:
    list: The merged sorted list
    """
    min_heap = []
    result = []

    # Initialize the heap with the first elements of each list, 
    # including the indices of the list and element.
    for idx, sublist in enumerate(lists):
        if sublist:
            heapq.heappush(min_heap, (sublist[0], idx, 0))

    # Process the heap to find the smallest element and append it to the result.
    while min_heap:
        val, list_idx, element_idx = heapq.heappop(min_heap)
        result.append(val)

        # If there are more elements in the list, push the next element onto the heap.
        if element_idx + 1 < len(lists[list_idx]):
            next_val = lists[list_idx][element_idx + 1]
            heapq.heappush(min_heap, (next_val, list_idx, element_idx + 1))

    return result

# Example input
lists = [[1, 4, 5], [1, 3, 4], [2, 6]]
merged_list = merge_k_lists(lists)
print(merged_list)  # Output: [1, 1, 2, 3, 4, 4, 5, 6]
