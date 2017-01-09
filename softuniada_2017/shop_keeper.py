products, orders = set([int(p) for p in input().split()]), [int(p) for p in input().split()]
if orders[0] not in products:
    print('impossible')
    exit()


aa = 0
for idx, order in enumerate(orders):
    if order not in products:
        # decide which product to remove
        to_remove = False
        to_add = False
        for p in products:
            if p not in orders[idx:]:
                to_remove = True
                to_add = True
                break
        if to_add and to_remove:
            products.remove(p)
            products.add(order)
            aa += 1


print(aa)
