# Inputs and valuables

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
alphabet = list(alphabet)
user_input = input("write your words: ")
user_input = list(user_input.upper())

# main part:lops in lops

b = []
for i in range(len(alphabet)):
    a = 0
    for g in range(len(user_input)):
        if alphabet[i] == user_input[g]:
            a += 1
    b.append(a)

# Finding the greatest

c = -1
d = 0
e = []
for i in range(len(b)):
    if b[i] > c:
        c = b[i]
        d = i
number = b.count(c)
# Running the program

if c > 1:
    print(f"Most frequent letter is {alphabet[d]} and {c} times")
if c == 1 or number >= 2:
    print("There is no most frequent letter!")
