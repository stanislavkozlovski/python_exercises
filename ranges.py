class Range:
    def __init__(self, _from, to):
        self._from = _from
        self.to = to

class BreakingRange:
    def __init__(self, value):
        self.value = value

# Sort the ranges by their start time
ranges = [Range(100, 200), Range(200, 300), Range(300, 400), Range(400, 500)]
# Sort the breaking ranges
breaking = [BreakingRange(101), BreakingRange(123), BreakingRange(151), BreakingRange(199), BreakingRange(311)]


valid_ranges = []
for curr_range in ranges:
    breaking_ranges_for_this_range = []  # store the breaking ranges for this specific range

    for breaking_range in breaking:  # go through each breaking range
        if breaking_range.value >= curr_range._from and breaking_range.value <= curr_range.to:
            # range is breaking
            breaking_ranges_for_this_range.append(breaking_range)
    if len(breaking_ranges_for_this_range) == 0:
        valid_ranges.append(curr_range)
        continue
    elif len(breaking_ranges_for_this_range) == 1:
        # Only one breaking range, split this one into two
        breaking_range = breaking_ranges_for_this_range[0]
        start_range = Range(curr_range._from, breaking_range.value)
        end_range = Range(breaking_range.value, curr_range.to)

        valid_ranges.append(start_range)
        valid_ranges.append(end_range)
    else:
        # Multiple breaking edges
        """
        Generate the start and end range, taking into account the first breaking and the last breaking
        After that, generate all the middle ranges which are in between the breaking ranges
        """
        first_breaking = breaking_ranges_for_this_range[0]
        last_breaking = breaking_ranges_for_this_range[len(breaking_ranges_for_this_range)-1]

        start_range = Range(curr_range._from, breaking_range.value)
        end_range = Range(breaking_range.value, curr_range.to)
        valid_ranges.append(start_range)
        valid_ranges.append(end_range)

        # generate all the in-between edges
        for i in range(0, len(breaking_ranges_for_this_range)-1):
            current_breaking_range = breaking_ranges_for_this_range[i]
            next_breaking_range = breaking_ranges_for_this_range[i + 1]
            # Build the between edge
            between_range = Range(_from=current_breaking_range.value + 1, to=next_breaking_range.value - 1)
            valid_ranges.append(between_range)

print(len(valid_ranges))