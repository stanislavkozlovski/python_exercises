#  https://www.hackerrank.com/challenges/hackerland-radio-transmitters


def main():
    n, k = [int(p) for p in input().split()]
    houses = sorted([int(p) for p in input().split()])
    transmitters_count = 0
    idx = 0
    while idx < len(houses):
        # get the furthest house from our point, that is where we'll put the transmitter
        transmitter_idx = find_furthest_house(houses, idx, transmitter_range=k)

        # get the furthest house from our transmitter which is in range, + 1 to get the next house
        # that is not covered. Then, on the next iteration, start searching from there
        next_search_idx = find_furthest_house(houses, transmitter_idx, transmitter_range=k) + 1

        transmitters_count += 1
        idx = next_search_idx

    print(transmitters_count)


def find_furthest_house(houses, idx, transmitter_range):
    """ Given the houses, return the INDEX of the furthest house that is in transmitter range"""
    house = houses[idx]
    furthest_house_idx = idx

    for new_idx in range(idx+1, len(houses)):
        new_house = houses[new_idx]
        house_distance = new_house - house
        if house_distance <= transmitter_range:
            furthest_house_idx = new_idx
        else:
            break

    return furthest_house_idx


if __name__ == '__main__':
    main()
