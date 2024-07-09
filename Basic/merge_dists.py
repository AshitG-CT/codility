'''Generate a Python code snippet to merge two dictionaries.'''
def merge_dicts(dict1, dict2):
    merge_dicts = dict1.copy()
    print('copy', merge_dicts)
    merge_dicts.update(dict2)
    return merge_dicts

dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3, 'd': 4}

merged_dict = merge_dicts(dict1, dict2)
print(merged_dict)  # Output: {'a': 1, 'b': 2, 'c': 3, 'd': 4}