data_structure = [[1, 2, 3], {'a': 4, 'b': 5}, (6, {'cube': 7, 'drum': 8}), "Hello", ((), [{(2, 'Urban', ('Urban2', 35))}])]

def calculate_structure_sum(*args):
    summa = 0
    if isinstance(args, (dict)):
        for key, value in args.items():
            summa += calculate_structure_sum(key)
            summa += calculate_structure_sum(value)

    elif isinstance(args, (list, tuple, set)):
        for item in args:
            summa += calculate_structure_sum(item)

    elif isinstance(args, (int, float)):
        summa += args

    elif isinstance(args, str):
        summa += len(args)
    return summa

result = calculate_structure_sum(data_structure)
print(result)