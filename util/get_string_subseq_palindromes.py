""" This basically returns a list of all the palindromes from subsequences of a string"""
def get_palindromes_for_string(string: str):
    if len(string) == 1:
        return [string]
    from pprint import pprint
    def get_i_j(l:list):
        len_l = len(l)
        if len_l == 2:
            return 0, 1
        if len_l % 2 == 0:
            return (len_l//2-1), len_l//2
        else:
            print(l)
            raise Exception('What THE FUCKK>?')

    incidence_matrix = []
    for _ in range(len(string)):
        incidence_matrix.append([False] * len(string))

    matches = {0: []}
    palindromes = []
    for row_idx in range(len(incidence_matrix)):
        for col_idx in range(len(incidence_matrix[row_idx])):
            if row_idx != col_idx and string[row_idx] == string[col_idx] and row_idx < col_idx:
                matches[0].append([row_idx, col_idx])
                palindromes.append(string[row_idx] + string[col_idx])

    for k in range(1, (len(string)//2)+1):
        for pal in matches[k-1]:
            i_idx, j_idx = get_i_j(pal)
            f_i, f_j = pal[i_idx], pal[j_idx]
            for o_pal in matches[0]:
                i, j = o_pal[0], o_pal[1]
                if i > f_i and j < f_j:
                    if k not in matches:
                        matches[k] = []
                    new_palindrome_indexes = pal[:i_idx+1] + [i, j] + pal[j_idx:]
                    matches[k].append(new_palindrome_indexes)
                    palindromes.append(''.join(string[p] for p in new_palindrome_indexes))
                    # matches[k].append([f_i, i, j, f_j])

    if len(string) % 2 != 0 and string == string[::-1]:
        palindromes.append(string)
    return palindromes + list(string)