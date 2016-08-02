"""
Shannon entropy was introduced by Claude E. Shannon in his 1948 paper "A Mathematical Theory of Communication".
Somewhat related to the physical and chemical concept entropy, the Shannon entropy measures the uncertainty
associated with a random variable, i.e. the expected value of the information in the message (in classical
informatics it is measured in bits). This is a key concept in information theory and has consequences for
things like compression, cryptography and privacy, and more.

The Shannon entropy H of input sequence X is calculated as -1 times the sum of the frequency
 of the symbol i times the log base 2 of the frequency:
            n
            _   count(i)          count(i)
H(X) = -1 * >   --------- * log  (--------)
            -       N          2      N
            i=1
"""
import math
from collections import Counter


def calculate_shannon_entropy_of_string(user_input: str) -> float:
    shannon_sum = sum(-1 * count_of_char/len(user_input) *
                    math.log2(count_of_char/len(user_input)) for _, count_of_char in Counter(user_input).items())
    return shannon_sum


print("{:.5f}".format(calculate_shannon_entropy_of_string("int main(int argc, char *argv[])")))
#  3.86673

print("{:.5f}".format(calculate_shannon_entropy_of_string("https://www.reddit.com/r/dailyprogrammer")))
#  4.05620

print("{:.5f}".format(calculate_shannon_entropy_of_string("563881467447538846567288767728553786")))
#  2.79421

print("{:.5f}".format(calculate_shannon_entropy_of_string("122333444455555666666777777788888888")))
#  2.79421