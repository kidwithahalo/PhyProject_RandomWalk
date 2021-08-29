'''Random walk in 1D
Body is initially resting at x = 0 and it will move
either in postive or negative x direction
'''


import random

def random_walk(n):

    x = 0
    for i in range(n):
        step = random.choice([-1,1])

        if step == -1:
            x = x-1
        else:
            x = x+1
    return (x)


number_of_walk = int(input("Number of walk : "))
walk_length = int(input("How long will be the walk : "))

for i in range(number_of_walk):
    walk = random_walk(walk_length)
    print(walk, "Distance from origin = ", abs(walk))

print(f"\nFinal distance from start: {abs(walk)} ")
