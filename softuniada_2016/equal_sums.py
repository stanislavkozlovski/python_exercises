num_a, num_b, num_c, num_d = int(input()),int(input()),int(input()),int(input())

sum_ab = num_a + num_b
sum_cd = num_c + num_d

sum_ac = num_a + num_c
sum_bd = num_b + num_d

sum_ad = num_a + num_d
sum_bc = num_b + num_c

sum_abc = sum_ac + num_b

sum_bcd = sum_bc + num_d

sum_acd = sum_ac + num_d

sum_abd = sum_ab + num_d

if sum_ab == sum_cd:
    print('Yes')
    print(sum_ab)
elif sum_ac == sum_bd:
    print('Yes')
    print(sum_ac)
elif sum_ad == sum_bc:
    print('Yes')
    print(sum_ad)
elif sum_abc == num_d:
    print('Yes')
    print(num_d)
elif sum_bcd == num_a:
    print('Yes')
    print(num_a)
elif sum_acd == num_b:
    print('Yes')
    print(num_b)
elif sum_abd == num_c:
    print('Yes')
    print(num_c)
else:
    print('No')