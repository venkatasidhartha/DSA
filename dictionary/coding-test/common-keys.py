
#  my solution
def merge_dicts(dict1, dict2):
    # TODO
    
    for key,value in dict2.items():
        if key in dict1:
            dict1[key] = dict1[key] + value
        else:
            dict1[key] = value
    return dict1
        
dict1 = {'a': 1, 'b': 2, 'c': 3}
dict2 = {'b': 3, 'c': 4, 'd': 5}
merge_dicts(dict1, dict2)


# SOLUTION - Time and Space Complexity of Common Keys
def merge_dicts(dict1, dict2):
    result = dict1.copy()
    for key, value in dict2.items():
        result[key] = result.get(key, 0) + value
    return result