vowels = {'a', 'e', 'i', 'o', 'u', 'y'}
word = input()

last_char = None
i = 0
is_beautiful = True
for char in word:
    current_char = char

    if (current_char in vowels and last_char in vowels) or (last_char == current_char):
        is_beautiful = False
        break

    last_char = current_char

print('Yes' if is_beautiful else 'No')