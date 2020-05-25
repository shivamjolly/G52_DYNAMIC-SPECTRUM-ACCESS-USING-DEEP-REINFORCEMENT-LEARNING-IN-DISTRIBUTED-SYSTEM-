import math
import random




#it is signal to noise ratio to calculate reward if there is no collision
# we have assumed it

sinr = 0.5

#claculating rewrd

x = math.log2(1+sinr)

# calculating true state at each iteration to maintain temporal coherence
# assuming different PU's will take different channel at different time

def truestate(state):
    inp = []
    for i in range(0, 22):
        x = random.randint(0, 1)
        inp.append(x)
    return inp[state]

 # In this we compare true state known in the environment with random state known by SU and give back reward

def take(z,j,state):

     # truestate known only at environment

       t = truestate(state)

    #this means if the bit value at zth coressponding channel  = 0 (it is not occupied)

       if z==0:

           # this means action = 0 (we are not occupying this channel)

              if j == 0:

                  # we are returning true state of that channel , reward = 0, collision = 0

                     return t,0,0

              # action = 1 (occupying that channel)

              else:

              # t=1 means it is occupied by a PU

                   if t==1:

                       # we are returning true state of that channel , reward = -2 because of collision, collision = 1

                            return t,-2,1
                   else:

                       # we are returning true state of that channel , reward = x because there is no collision and SU has occupied it, collision = 0

                          return 1,x,0

     # z==1 means SU assumes that it is already occupied by PU

       else:

           # we are returning 1 as there will no change in SU state , reward = 0, collision = 0

              return 1,0,0
