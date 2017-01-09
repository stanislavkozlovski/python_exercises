"""
Emma is playing a new mobile game involving n clouds numbered from 0 to n-1.
A player initially starts out on cloud C0, and they must jump to cloud Cn-1.
In each step, she can jump from any cloud i to cloud i+1 or cloud i+2.

There are two types of clouds, ordinary clouds and thunderclouds.
The game ends if Emma jumps onto a thundercloud, but if she reaches the last cloud, she wins the game!

Input Format

The first line contains an integer, N (the total number of clouds).
The second line contains N space-separated binary integers describing clouds [C0,...Cn-1]
"""
THUNDERCLOUD_KEY = '1'
_ = input()
clouds = input().split()
idx, steps = 0, 0
end_index = len(clouds) - 1

while idx != end_index:
    idx += 2
    if idx > end_index or clouds[idx] == THUNDERCLOUD_KEY:  # out of range or hit a thundercloud
        idx -= 1
    steps += 1

print(steps)