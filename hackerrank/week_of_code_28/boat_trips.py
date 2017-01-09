def check_trips(total_passengers_per_trip: int):
    for passengers_count in (int(p) for p in input().split()):
        if passengers_count > total_passengers_per_trip:
            return False
    return True


def main():
    trip_count, boat_capacity, boat_count = [int(p) for p in input().split()]
    total_passengers_per_trip = boat_capacity * boat_count
    print('Yes' if check_trips(total_passengers_per_trip) else 'No')


if __name__ == '__main__':
    main()
