from queue import deque

dp = {}

def sol_1():
    idx = 0
    while True:
        min_idx = get_min_char_idx(s, idx)
        if min_idx == -1:
            break
        if len(t) > 0 and ord(t[-1]) <= ord(s[min_idx]):
            # we need to take t
            u.append(t.pop())
        else:
            # take up to min_idx
            t.extend(s[idx:min_idx+1])
            idx = min_idx+1

def efficient_sol():
    global u, t, s
    import string
    indices = {char: [] for char in string.ascii_lowercase}  # will hold indices for each char

    # fill indices
    for idx, char in enumerate(s):
        indices[char].append(idx)

    curr_idx = 0
    for char in string.ascii_lowercase:
        if curr_idx == len(s):
            break
        if len(t) > 0 and ord(char) >= ord(t[-1]):
            # We've started searching for bigger characters, so we need to empty the smaller ones first
            while len(t) > 0 and ord(char) >= ord(t[-1]):
                u.append(t.pop())

        for idx in sorted(indices[char]):
            if curr_idx == len(s):
                return
            min_idx = idx
            if min_idx < curr_idx:
                # we've passed this character
                continue
            elif min_idx == curr_idx:
                if len(t) > 0 and ord(char) > ord(t[-1]):
                    raise Exception()
                # we are at that character, so just add it
                u.append(char)
                curr_idx += 1
                continue
            # mid_idx is bigger, so we put everything up until this character in T
            # then, add the character himself
            t.extend(s[curr_idx:min_idx])
            u.append(char)
            curr_idx = min_idx + 1
    while curr_idx < len(s):
        pass

def get_min_char_idx(s: str, start_idx: int):
    global dp
    if start_idx >= len(s):
        return -1
    if start_idx in dp:
        return dp[start_idx]
    min_char = s[start_idx]
    min_idx = start_idx
    while start_idx < len(s):
        if ord(s[start_idx]) < ord(min_char):
            min_char = s[start_idx]
            min_idx = start_idx
        start_idx += 1
    dp[start_idx] = min_idx
    return min_idx

# aaaczbgjs
import string
s = input()
# s = 'abcadc'
# s = string.ascii_lowercase + string.ascii_lowercase

u = []
t = []

# if len(s) >= 10**3:
efficient_sol()
# else:
#     sol_1()

# abaaabababacba
# print(t)
print(''.join(u + list(reversed(t))))
