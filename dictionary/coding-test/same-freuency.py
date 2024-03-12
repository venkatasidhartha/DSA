

def check_same_frequency(list1, list2):
    
    def countCheck(lst):
        result = {}
        for i in lst:
            if i not in result:
                result[i] = lst.count(i)
        return result

    return countCheck(list1) == countCheck(list2) 


list1 = [1, 2, 3, 2, 1]
list2 = [3, 1, 2, 1, 3]
print(check_same_frequency(list1, list2))