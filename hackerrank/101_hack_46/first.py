j = int(input())
cupcakes = [int(p) for p in input().split()]
sum = 0
for idx, cup in enumerate(reversed(sorted(cupcakes))):

    sum += (2**idx * cup)
print(sum)
