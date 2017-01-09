n = int(input())

width = (n*2)-1
# roof

dots_len = n-1
print('.' * dots_len + '*' + '.' * dots_len)
dots_len -= 1
space_len = 1
for i in range(n-2):
    print('.' * dots_len + '*' + ' '*space_len + '*' + '.' * dots_len)

    dots_len -= 1
    space_len += 2
print(('* '*n)[:-1])

# basics
top = '+' + '-'*(width-2) + '+'
print(top)
for i in range(n-2):
    print('|' + ' '*(width-2) + '|')
bot = top
print(bot)