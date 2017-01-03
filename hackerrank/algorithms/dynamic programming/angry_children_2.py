n = int(input())
k = int(input())
sset = []
for _ in range(n):
    sset.append(int(input()))

sset = list(sorted(sset))
new = []
for idx in range(0, len(sset)-1):
    new.append(abs(sset[idx]-sset[idx+1]))

# print(new)
import sys
smallest_sum, idx = sys.maxsize,0

new_k = k-1
for i, el in enumerate(new):
    if i == (len(new) - new_k)+1:
        break
    current_sum = sum(new[i:i+new_k])
    # current_sum = el + sum(new[i+1:i+(new_k)])
    if current_sum < smallest_sum:
        smallest_sum = current_sum
        idx = i

# print(idx)
# print(smallest_sum)

numbers = sset[idx:idx+k]
# print(numbers)

unfairness = 0
for idx, num in enumerate(numbers):
    unfairness += sum(abs(num-numbers[j]) for j in range(idx+1, len(numbers)))
print(unfairness)