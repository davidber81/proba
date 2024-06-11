data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]

def calculate_structure_sum(structure):
    total_sum = 0
    for current in structure:
        if isinstance(current, list):
            total_sum += calculate_structure_sum(current)
        elif isinstance(current, tuple):
            total_sum += calculate_structure_sum(current)
        elif isinstance(current, set):
            total_sum += calculate_structure_sum(current)
        elif isinstance(current, dict):
            k, v = current.keys(), current.values()
            total_sum += calculate_structure_sum(k)
            total_sum += calculate_structure_sum(v)
        elif isinstance(current, int):
            total_sum += current
        elif isinstance(current, str):
            total_sum += len(current)
    return total_sum

result = calculate_structure_sum(data_structure)
print(result)