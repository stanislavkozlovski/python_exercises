def word_is_valid(word):
    if len(word) == 0:
        return 'Valid'
    last_chr = word[0]

    for i in range(1, len(word)):
        current_chr = word[i]
        if last_chr == current_chr:
            return i-1
        last_chr = current_chr

    return 'Valid'

st = input()

operations = 0
invalid_index = word_is_valid(st)
while invalid_index != 'Valid':
    operations += 1
    st = st[:invalid_index] + st[invalid_index+2:]
    invalid_index = word_is_valid(st)

if st == '':
    print('Empty String')
else:
    print(st)
print('{} operations'.format(operations))
