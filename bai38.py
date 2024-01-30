dict1 = {'a': 1, 'b': 2, 'c': 3}
dict2 = {'b': 3, 'c': 4, 'd': 5}
def merge_and_sum(dict1, dict2):
    merged_dict = {}
    for key in dict1:
        if key in dict2:
            merged_dict[key] = dict1[key] + dict2[key]
        else:
            merged_dict[key] = dict1[key]
    for key in dict2:
        if key not in dict1:
            merged_dict[key] = dict2[key]
    return merged_dict
merged = merge_and_sum(dict1, dict2)
print(merged)