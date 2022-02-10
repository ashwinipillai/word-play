# Import the modules required
import json
import enchant
from itertools import permutations

def word_exists(w):
    # converts to lower case
    obj = enchant.Dict("en_US")
    check_status = obj.check(w)
    if check_status:
        return w;


# Driver code
# print("How many letters do you want to play the Jumble Game for?")
# no_of_letters = int(input())
# letters = ''.join((random.choice(string.ascii_lowercase) for x in range(no_of_letters)))
print("Enter letters: ")
letters = input().split(" ")
all_permutations =[''.join(p) for p in permutations(letters)]
for each_combination in all_permutations:
    output = word_exists(each_combination)
    if output:
        print(output)
