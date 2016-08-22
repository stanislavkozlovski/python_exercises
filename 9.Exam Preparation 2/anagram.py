"""
Given a path to a text file, whose contents are one word per line. Find the anagrams of a given word.

sample input:
./words.txt
horse
"""
from collections import Counter


def is_anagram(str1: str, str2: str):
    return Counter(str1.lower()) == Counter(str2.lower())

try:
    file_path = input()
    word = input()
    anagram_list = []

    with open(file_path, encoding='utf-8') as file_reader:
        for potential_anagram in file_reader.read().splitlines():
            if potential_anagram != word and is_anagram(word, potential_anagram):
                anagram_list.append(potential_anagram)

    print('\n'.join(sorted(anagram_list))) if anagram_list else print("NO ANAGRAMS")
except:
    print("INVALID INPUT")

# 100/100

