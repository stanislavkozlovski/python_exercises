def is_abbreviatable(a, b):
    if len(b) > len(a):
        return False

    a_mark, b_mark = 0, 0
    lower = 0

    while a_mark < len(a):
        if b_mark >= len(b):
            if a[a_mark].isupper():
                return False
            else:
                a_mark += 1
        else:
            a_chr = a[a_mark]
            b_chr = b[b_mark]

            # try to match the equal case
            if a_chr == b_chr:
                a_mark += 1
                b_mark += 1
                lower = b_mark  # go back if we've found two equal upper case words
            elif lower < len(b) and a_chr.islower() and (a_chr.upper() == b[lower]):
                a_mark += 1
                lower += 1
            elif a_chr.isupper():
                # possible violation
                if b_mark <= lower:
                    b_mark += 1
                else:
                    return False
            else:
                a_mark += 1
    return b_mark >= len(b) or lower >= len(b)

for _ in range(int(input())):
    a, b = input(), input()
    print('YES' if is_abbreviatable(a, b) else 'NO')
