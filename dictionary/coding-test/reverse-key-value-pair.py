
# my solution

def reverse_dict(my_dict):
    # TODO
    result = {}
    for key,value in my_dict.items():
        # print(key,value)
        result[value]=key
    return result


my_dict = {'a': 1, 'b': 2, 'c': 3}
reverse_dict(my_dict)