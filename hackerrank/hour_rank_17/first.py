_, k = [int(p) for p in input().split()]
hurdles = [int(p) for p in input().split()]
maxx = max(hurdles)
if maxx > k:
    print(maxx-k)
else:
    print(0)