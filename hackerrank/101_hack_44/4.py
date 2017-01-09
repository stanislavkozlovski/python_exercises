#
# def countPS(string):
#     n = len(string)
#     cps = [[0] * (n+n) for _ in range(n+2)]
#     for i in range(n):
#         cps[i][i] = 1
#
#     for l in range(2, n+1):
#         for i in range(n):
#             k = l + i - 1
#             if k < len(string) and string[i] == string[k]:
#                 cps[i][k] = cps[i][k-1] + cps[i+1][k] + 1
#             else:
#                 cps[i][k] = cps[i][k-1] + cps[i+1][k] - cps[i+1][k-1]
#     return cps[0][n-1]
#
#
# def shift_letter(letter, times_to_shift):
#     ascii_num = ord(letter)
#     ascii_num += times_to_shift
#     if ascii_num > 122:
#         ascii_num = 96 + (ascii_num-122)
#     return chr(ascii_num)
#
#
# def main():
#     n, query_count = [int(part) for part in input().strip().split()]
#     string = input().strip()
#     modulo_val = 1000000007
#     for _ in range(query_count):
#         user_input = input().split()
#         if len(user_input) == 4:
#             # Type 1
#             _useless, i, j, t = [int(part) for part in user_input]
#             shift = t % 26  # times to shift
#             new_string = string[0:i]
#             for part in string[i:j+1]:
#                 new_string += shift_letter(part, shift)
#             new_string += string[j+1:]
#             string = new_string
#         else:
#             # type 2
#             _useless, i, j = [int(part) for part in user_input]
#             substring_ = string[i:j+1]
#             palindrome_count = countPS(substring_)
#             print(palindrome_count % modulo_val)
#
# if __name__ == '__main__':
#     main()

#!/bin/python3

import sys


n,q = input().strip().split(' ')
n,q = [int(n),int(q)]
s = input().strip()
sa = [ord(i) - ord('a') for i in s]
for a0 in range(q):
    qu = input().strip().split(' ')
    if int(qu[0]) == 1:
        start = int(qu[1])
        end =int(qu[2])
        t = int(qu[3])
        for i in range(start, end + 1):
            sa[i] = (sa[i] + t) % 26
    else:
        start = int(qu[1])
        end =int(qu[2])
        d = [0] * 27
        for i in range(start, end + 1):
            d[sa[i]] += 1
        ans = 1
        for i in range(27):
            if d[i]:
                ans = (ans * pow(2, d[i] - 1) )% 1000000007
        g = ans
        ans = (ans - 1 )% 1000000007
        for i in range(27):
            if d[i]:
                ans = (ans + g) % 1000000007

        print(ans)