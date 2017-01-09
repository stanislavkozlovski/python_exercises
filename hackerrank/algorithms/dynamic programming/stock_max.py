#  https://www.hackerrank.com/challenges/stockmax


# get the index of the maximum number and the index of the maximum number after it
def get_max_and_next_max_idx(arr):
    max_num, next_max = 0, 0
    m_idx, nm_idx = -1, -1
    for idx, num in enumerate(arr):
        if num > max_num:
            max_num = num
            m_idx = idx
            nm_idx, next_max = -1, -1
        elif num > next_max:
            nm_idx = idx
            next_max = num

    return m_idx, nm_idx


def get_profit(arr):
    max_idx, next_max_idx = get_max_and_next_max_idx(arr)
    profit = 0
    stock_count, money_invested = 0, 0
    for idx in range(len(arr)):
        stock_price = arr[idx]
        if idx == max_idx:
            # SELL
            profit += (stock_count * stock_price) - money_invested
            stock_count, money_invested = 0, 0
            if max_idx == next_max_idx:
                idx_to_add = next_max_idx
                max_idx, next_max_idx = get_max_and_next_max_idx(arr[next_max_idx+1:])
                max_idx += idx_to_add + 1
                next_max_idx += idx_to_add + 1
            else:
                max_idx = next_max_idx

        elif idx < max_idx:
            # BUY
            stock_count += 1
            money_invested += stock_price

    return profit


def main():
    test_case_count = int(input())
    for _ in range(test_case_count):
        _ = input()
        nums = [int(part) for part in input().split()]
        print(get_profit(nums))


if __name__ == '__main__':
    main()