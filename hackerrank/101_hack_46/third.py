_ = input()

substrs = input().split()
orig_powers = [int(p) for p in input().split()]
n = int(input())
strrr = []
for _ in range(n):
    start, end, sbstr = input().split()
    start = int(start)
    end = int(end)
    powers = {}
    for idx in range(start, end+1):
        strength = orig_powers[idx]
        if substrs[idx] not in powers:
            powers[substrs[idx]] = []
        powers[substrs[idx]].append(strength)

    # iterate through substr
    overall_str = 0
    MAX_POWER_LEN = next(reversed(sorted([len(key) for key in powers.keys()])))
    # print("MAX POWER LEN IS ", MAX_POWER_LEN)
    for idx, chr in enumerate(sbstr):
        curr_sbstr = chr
        if curr_sbstr in powers:
            overall_str += sum(powers[curr_sbstr])
        for idx_2 in range(idx+1, len(sbstr)):
            curr_sbstr += sbstr[idx_2]
            if len(curr_sbstr) > MAX_POWER_LEN:
                break
            if curr_sbstr in powers:
                overall_str += sum(powers[curr_sbstr])
    strrr.append(overall_str)

print("{} {}".format(min(strrr), max(strrr)))
# print(powers)