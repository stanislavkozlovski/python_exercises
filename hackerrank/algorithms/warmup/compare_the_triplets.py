"""
Alice and Bob each created one problem for HackerRank.
A reviewer rates the two challenges, awarding points on a scale from 1 to 100 for three categories: problem clarity,
 originality, and difficulty.

We define the rating for Alice's challenge to be the triplet A = (a0, a1, a2),
and the rating for Bob's challenge to be the triplet B = (b0, b1, b2).

Your task is to find their comparison scores by comparing  a0 with b0, a1 with b1, and a2 with b2.

If a>b, then Alice is awarded 1 point.
If a < b, then Bob is awarded 1 point.
If a==b, then neither person receives a point.
Given A and B, can you compare the two challenges and print their respective comparison points?

Input Format

The first line contains 3 space-separated integers, a0, a1, and a2, describing the respective values in triplet .
The second line contains 3 space-separated integers, b0, b1, and b2, describing the respective values in triplet .

Constraints
1 <= Ai <= 100
1 <= Bi <= 100

Output Format
Print two space-separated integers denoting the respective comparison scores earned by Alice and Bob.


"""
a0, a1, a2 = [int(num) for num in input().split()]
b0, b1, b2 = [int(num) for num in input().split()]

alice = sum([a0 > b0, a1 > b1, a2 > b2])
bob = sum([b0 > a0, b1 > a1, b2 > a2])
print("{alice} {bob}".format(alice=alice, bob=bob))