def get_all_substrings(input_string):
  length = len(input_string)
  return [input_string[i:j+1] for i in range(length) for j in range(i,length+1)]

number = input()
count = 0
# print(get_all_substrings(number))
for substr in get_all_substrings(number):
    count += 1 if ((int(substr) % 6) == 0 and substr[0] != '0') or (substr == '0') else 0
print(count)
# print(sum([True for a in get_all_substrings(number) if (int(a) % 6 == 0 and a[0] != '0' or (a == '0'))]))