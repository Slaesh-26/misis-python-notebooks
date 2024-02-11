import re

def get_word_count(word, file_name):
    file = open(file_name, 'r', encoding = "utf-8")
    file_str = file.read()
    words = re.findall(r'[A-Za-zА-Яа-я]+', file_str)

    count = words.count(word)
    file.close()
    return count

def word_frequency(phrase):
    phrase = phrase.lower()
    match = re.split(r'\W+', phrase)
    dict = {}
    for word in match:
        count = dict.get(word, 0)
        dict.update({word: count + 1})
    
    return dict

def get_most_frequent_word(phrase):
    frequency_dict = word_frequency(phrase)
    max_count = 0
    max_count_key = ""
    for key, value in frequency_dict.items():
        if (value > max_count):
            max_count = value
            max_count_key = key

    return max_count_key

def get_longest_word(phrase):
    phrase = phrase.lower()
    match = re.split(r'\W+', phrase)
    max_length = 0
    max_length_word = ""
    
    for word in match:
        if max_length < len(word):
            max_length = len(word)
            max_length_word = word
    
    return max_length_word