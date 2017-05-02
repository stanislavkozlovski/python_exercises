# https://www.hackerrank.com/challenges/richie-rich


def get_mirror_idx(idx: int, arr_len: int):
    """ Returns the mirrored index of an array """
    return arr_len - idx - 1
_, changes_count = [int(p) for p in input().split()]
word = list(input())
changed_indices = set()

"""
Algo is the following:
    Greedily change the first-most indices to create the palindrome
    Then, if we have moves to spare, we modify the changes we made to create the biggest number
"""

idx = 0
changes_made = 0
word_len = len(word)
while idx < len(word) // 2:
    mirror_idx = get_mirror_idx(idx, word_len)
    if word[idx] != word[mirror_idx]:
        if changes_made >= changes_count:
            print(-1)
            exit()  # this string cannot be changed into a palindrome with the given allowed changes

        # Change the indices to the biggest possible
        changed_indices.add(idx)
        bigger_num = max(word[idx], word[mirror_idx])
        word[idx], word[mirror_idx] = bigger_num, bigger_num
        changes_made += 1
    idx += 1

# The string is now a palindrome, use the leftover changes to transform it into the biggest possible
idx = 0
while idx < len(word) // 2 and changes_made < changes_count:
    leftover_changes = changes_count - changes_made
    if word[idx] != '9':  # we want to change these, since they're not the biggest possible
        mirror_idx = get_mirror_idx(idx, word_len)
        if idx not in changed_indices and mirror_idx not in changed_indices and leftover_changes >= 2:
            # This will take two changes, since we have not changed them at all
            word[idx], word[mirror_idx] = '9', '9'
            changes_made += 2
        elif idx in changed_indices or mirror_idx in changed_indices and leftover_changes >= 1:
            #  these have been changed, so we can use one more change to make them equal to 9
            # (as if reverting the prev one)
            word[idx], word[mirror_idx] = '9', '9'
            changes_made += 1
    idx += 1

if changes_made < changes_count and len(word) % 2 != 0:  # change mid idx
    word[len(word) // 2] = '9'

print(''.join(word))