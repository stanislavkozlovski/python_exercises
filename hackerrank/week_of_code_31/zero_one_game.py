def element_exists(nums: list):
    """
    Validates that a valid element with two zeroes exists at all
    :return:
    """
    has_valid = False
    for idx in range(1, len(nums)-1):
        if nums[idx-1] == 0 and nums[idx+1] == 0:
            has_valid = True
    return has_valid


def get_valid_moves_indices(nums: list, wanted_num) -> set():
    """ Returns a list - the indices of valid moves taking '0' or valid moves taking '1',
        depending on the wanted_num """
    valid_indices = set()
    for idx in range(1, len(nums)-1):
        if nums[idx-1] == 0 and nums[idx+1] == 0 and nums[idx] == wanted_num:
            valid_indices.add(idx)
    return valid_indices


def rebuild_nums(nums, forbidden_indices):
    """
    Rebuild the nums while not adding the forbidden indices
    """
    new_nums = []
    for idx, num in enumerate(nums):
        if idx in forbidden_indices:
            continue
        new_nums.append(num)
    return new_nums


for q in range(int(input())):
    input()
    nums = [int(p) for p in input().split()]
    if not element_exists(nums):
        print('Bob')
        continue
    moves_processed = 0
    # Get all the indices of valid moves where the number is 1
    valid_one_indices = get_valid_moves_indices(nums, 1)
    moves_processed += len(valid_one_indices)
    # Remove all those 1 indices in the nums
    nums = rebuild_nums(nums, valid_one_indices)
    # Get all the indices of valid moves where the number is 0
    moves_processed += len(get_valid_moves_indices(nums, 0))

    if moves_processed % 2 == 0:
        print('Bob')
    else:
        print('Alice')
