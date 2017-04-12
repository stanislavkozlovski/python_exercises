def get_removable_indices(string: str):
    valid_indices = set()
    last_idx = None  # use this to keep track of repeating words, i.e "aaa" - we should only get [0, 1] as indices
    for idx in range(1, len(string)):
        if string[idx] == string[idx-1] and last_idx != idx-1:
            last_idx = idx
            valid_indices.add(idx-1)
            valid_indices.add(idx)
    return valid_indices


def rebuild_string(string, removed_indices):
    """ Rebuild the string, while not adding the indices that were removed """
    return ''.join(string[idx] for idx in range(len(string)) if idx not in removed_indices)


string = input()
indices_to_remove = get_removable_indices(string)
while indices_to_remove:
    indices_to_remove = get_removable_indices(string)
    string = rebuild_string(string, indices_to_remove)

print(string if string else 'Empty String')