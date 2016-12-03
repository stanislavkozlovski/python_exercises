def get_min_packages(n, m):
    if n == 1 or m == 1 and n != m:
        if max(n, m) % 2 == 0:
            return max(n,m) // 2
        else:
            return ((max(n,m)) // 2) + 1
    if n % 2 == 0 and m % 2 == 0:
        return (n*m)//4
    elif n % 2 == 0 or m % 2 == 0:
        even_num = n if n % 2 == 0 else m
        odd_num = n if n % 2 != 0 else m

        if even_num > odd_num:
            return get_min_packages(even_num, odd_num+1)
        else:
            # ex 4, 7
            # convert odd to even
            odd_num -= 1
            # 4, 6 => (6*4) / 4
            return get_min_packages(even_num, odd_num) + (even_num//2)
    else:
        # BOTH ARE ODD
        if n == m:
            return get_min_packages(n-1, m-1) + (n*2)//2
        else:
            return get_min_packages(n-1, m-1) + ((n + m) // 2)
if __name__ == '__main__':
    n, m = [int(piece) for piece in input().split()]
    print(get_min_packages(n, m))