# https://www.hackerrank.com/challenges/candies
line_count = int(input())

last_child_value = 0
last_candy = 0
candy_sum = 0
ratings, candies = [], []
# this loop will assure that the candies are bigger in the ascending order, but it does not handle the descending nodes
"""
ex: [3,2,1] -> this loop will return [1,1,1] candies
but in [1,2,3] -> this loop will return [1,2,3] candies
"""
for idx in range(line_count):
    child_rating = int(input())
    current_candy = 1  # we always want to give the minimum number of candies
    if child_rating > last_child_value:
        # if the next child has a bigger rating, it must have more than the current one
        current_candy = last_candy + 1

    candy_sum += current_candy
    last_candy = current_candy
    last_child_value = child_rating
    ratings.append(child_rating)
    candies.append(current_candy)

"""
to combat the [3,2,1] scenario in the loop above, we loop backwards, this time incrementing the candies
in a 'descending order'
"""
# we go back the ratings to fix any inconsistencies
for i in reversed(range(0, line_count-1)):
    if ratings[i] > ratings[i + 1]:
        this_candy = candies[i]
        next_candy = candies[i + 1]
        if this_candy <= next_candy:
            # the rank at i is bigger than the rank at i+1, but he does not have more candies
            difference_to_add = (next_candy - this_candy) + 1
            this_candy += difference_to_add

            # we increase the candies at i and add them
            candies[i] = this_candy
            candy_sum += difference_to_add

print(candy_sum)