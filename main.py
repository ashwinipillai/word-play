# Import the modules required
import json
import enchant
from itertools import permutations


def convertTuple(tup):
    # initialize an empty string
    str = ''
    for item in tup:
        str = str + item
    return str

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
print("Enter letters separated by SPACE ; Press ENTER when you are done. ")
letters = input().split(" ")
all_permutations=[]

for a in range(3,len(letters)+1):
    words = list(permutations(letters,a))
    for w in words:
        all_permutations.append(convertTuple(w))
for each_combination in all_permutations:
    output = word_exists(each_combination)
    if output:
        print(output)