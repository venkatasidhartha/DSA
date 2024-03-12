
#  Creating Dictionary
my_dict = dict() # O(1)
print(my_dict)

mydict2 = {} # O(1)
print(mydict2)

"""
To creating a empty Dict
Time Complexity : O(1)
Space Complexity : O(1)
"""

eng_sp = dict(one='uno',two='doc',three='tres')
print(eng_sp)

eng_sp2 = {"one":'uno',"two":'doc',"three":'tres'}
print(eng_sp2)

"""
Insert Records
Time Complexity : O(n)
Space Complexity : O(n)
"""


# converting list of tuple pair into dict

eng_sp3 = [("one",'uno'),("two",'doc'),("three",'tres')]
print(dict(eng_sp3))

"""
Converting tuple into dict and Insert Records
Time Complexity : O(n)
Space Complexity : O(n)
"""



# Dictionaries in memory
"""
A hash table is a way of doing key-value lookups. you store the values in an array, and then use a
has function to find the index of the array cell that corresponds to your key-value pair
"""

# Insert/Update a dict

myDict = {"name":"edy","age":26}
myDict["age"] = 28 # O(1)
myDict["address"] = "sevenwells" # O(1)
print(myDict)

"""
Insert Records
Time Complexity : O(1)
Space Complexity : amortized O(1)
"""

# Iterating a dict

def iterateDict(dict):
    for key in dict:
        print(key,dict[key]) 
iterateDict(myDict)

"""
Iterating a dict
Time Complexity : O(n)
Space Complexity : O(1)
"""

# searching element

def searchDict(dict,value):
    for key in dict:
        if dict[key] == value:
            return key,value
    return 'Not found'
print(searchDict(myDict,'edy'))

"""
search element in dict with leiner search
Time Complexity : O(n)
Space Complexity : O(1)
"""

# Delete/Remove element

# using del method
del myDict["age"]
print(myDict)

# using pop method
removedelement = myDict.pop('name') # O(1)
print(removedelement)

# using popitem
removedelement = myDict.popitem() # O(1)
# this will remove the last element in the Dict
print(removedelement)

# using clear method
myDict.clear() # O(n)
# this function will clear all the elements in the dict
print(myDict)

# dict methods

my_dict = {
    "apple": 3,
    "banana": 5,
    "orange": 7,
    "grape": 9,
    "kiwi": 2,
    "watermelon": 8,
    "pineapple": 4,
    "strawberry": 6,
    "blueberry": 1,
    "mango": 10
}

# copy method
coptDict = my_dict.copy() #O(n)
print(coptDict)

# fromkeys() method
# this methid is use to create dict with the keys and same value or not
newDict = {}.fromkeys([1,2,3],0)
print(newDict)

# get method
# this method is use to get a element in dict
# syntax : dict.get(key,value) value is to set default value if the key is not there in dict,
# if value is not specified it will return None
print(my_dict.get("apple",32))


# items() method
# this method will return key and value as list of tuples
print(my_dict.items())
"""
output
dict_items([('apple', 3), ('banana', 5), ('orange', 7), ('grape', 9), ('kiwi', 2), ('watermelon', 8), ('pineapple', 4), ('strawberry', 6), ('blueberry', 1), ('mango', 10)])
"""

# keys() method
#  this method return list of keys in dict
print(my_dict.keys())
"""
output
dict_keys(['apple', 'banana', 'orange', 'grape', 'kiwi', 'watermelon', 'pineapple', 'strawberry', 'blueberry', 'mango'])
"""

# popitem() method
# this will remove the last element of the dict
print(my_dict.popitem())
"""
output
('mango', 10)
"""

# setdefault() method
# syntax: dict.setdefault(key,default_value)
# this method will search the key in dict, if the key is not present in dict it will create a key and value 
print(my_dict.setdefault("apples",'sds'))

# pop method
# syntax: dict.pop(key,default_value)
#  this method will also works like the setdefault() method like search but difference is it will remove the element from the dict
# if the key is not there it will return default_value which we declear
print(my_dict.pop("apples",'sds'))


# values() method
#  this method return list of values in dict
print(my_dict.keys())
"""
output
dict_keys(['apple', 'banana', 'orange', 'grape', 'kiwi', 'watermelon', 'pineapple', 'strawberry', 'blueberry'])
"""

# update method
# this method will update the dict with another dict 
#  the dict as same key it will update the value of the key in dict
# this method will take tuples or another dict as argument
my_dict.update({"asd":"dfd"})
my_dict.update([("dfd","ewre")])
print(my_dict)


# dict operations
# in operation
print('apple' in my_dict)
# In operation will works whith keys not with values
# not in operation
print('apple' not in my_dict)
# returns boolean
"""
output 
True 
"""
# len() operation
print(len(my_dict))
# len will take each pair into one item
"""
output
11
"""
# all() operation
print(all(my_dict))
# not muched used


# sorted operation
print(sorted(my_dict))
# this operation will return the list of key's in sorted order
"""
output
['apple', 'asd', 'banana', 'blueberry', 'dfd', 'grape', 'kiwi', 'orange', 'pineapple', 'strawberry', 'watermelon']
"""


"""
Operation                               Time Complecity     Space Complecity

creating an dict                            O(len(dict))        O(N)
inserting a value in an dict                O(1)/O(n)           O(1)
traversing a dict                           O(N)                O(1)
accessing a cell                            O(1)                O(1)
searching a value                           O(N)                O(1)
deleting a value                            O(1)                O(1)


"""