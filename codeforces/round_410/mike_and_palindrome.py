def is_almost_palindrome(word: str):
    diff_count = 0
    left_idx = 0
    right_idx = len(word) - 1
    while left_idx < right_idx:
        if word[right_idx] != word[left_idx]:
            diff_count+= 1
        right_idx -= 1
        left_idx += 1
    if diff_count == 1 or (diff_count == 0 and right_idx == left_idx):
        return True
    return False

print('YES' if is_almost_palindrome(input()) else 'NO')