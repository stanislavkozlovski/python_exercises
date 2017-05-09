class Person:
    def __init__(self, pos, value):
        self.pos = pos
        self.value = value

    def __gt__(self, other):
        return self.pos > other.pos

class Saleswoman:
    def minMoves(self, pos, delta):
        pos = pos
        vals = delta

        peple = []
        for idx in range(len(pos)):
            peple.append(Person(pos[idx], vals[idx]))
        peple = sorted(peple)

        curr_value = 0
        min_idx, owed = None, 0
        curr_idx = 0
        moved = 0
        for idx, prsn in enumerate(peple):
            moved += prsn.pos - curr_idx
            curr_idx = prsn.pos
            if prsn.value < 0:

                if abs(prsn.value) <= curr_value and owed == 0:
                    # pay him
                    curr_value += prsn.value  # pay
                else:
                    owed += abs(prsn.value)
                    if min_idx == None:
                        min_idx = curr_idx
            else:
                curr_value += prsn.value

                if owed <= curr_value and owed > 0:
                    # we have enough to pay back, so pay back
                    curr_value -= owed

                    moved += (curr_idx - min_idx) * 2  # back and forth
                    min_idx = None
                    owed = 0
        return moved

# print(minMoves([3,14,15,92,101], [-3,2,3,-3,1]))
# print(minMoves([1,2,4,8,16,32,64,128], [-1,-1,-1,-1,1,1,1,1]))
# print(minMoves([100000], [0]))
# print(minMoves([100,200,300,400], [10,-3,-5,2]))
# print(minMoves([1,2,3,5,8,13,21,34,55,89], [-1,1,-1,1,-1,1,-1,1,-1,1]))
# print(Saleswoman().minMoves([1,2,3,6,10,15,21,28,36,45,55], [-3,-5,10,-2,-6,-7,3,-2,8,5,-1]))