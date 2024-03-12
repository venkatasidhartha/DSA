
# my solution
def count_word_frequency(words):
    my_dict = {}
    for word in words:
        my_dict[word] = words.count(word)
    print(my_dict)

words = ['apple', 'orange', 'banana', 'apple', 'orange', 'apple'] 
count_word_frequency(words) 


# SOLUTION - Time and Space Complexity of Count Word Frequency
def count_word_frequency(words):
    word_count = {}
    for word in words:
        word_count[word] = word_count.get(word, 0) + 1
    return word_count