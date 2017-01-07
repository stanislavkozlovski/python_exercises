n = int(input())
width = n*2+1
height = n
top = '.' * (n-1) + '_/_' + '.' * (n-1)
print(top)
head = '/' + ('.'*((width-5)//2)) + '^,^' + ('.'*((width-5)//2)) + "\\"
bot = '\\' + ('.'*((width-5)//2)) + '\\_/' + ('.'*((width-5)//2)) + "/"

print(head)
for i in range(height-3):
    print('|' + '.'*(width-2) + '|')
print(bot)