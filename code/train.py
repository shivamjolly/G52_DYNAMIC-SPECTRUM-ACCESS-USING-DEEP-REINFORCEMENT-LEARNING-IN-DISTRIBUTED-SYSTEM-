import numpy as np
import random
import plotting as pl
import environment as en

#total channels

n_channel = 22

alpha = 0.01    #learning rate
gamma = 0.6     #discounted rate
qtable = np.zeros([22, 2])           #q-value table

#total reward list

RR = []

#collision rate list

CC= []

# to calculate random states of channels


def DQN():
    inp = []
    R = 0
    C=0
    for i in range(0, n_channel):

        x = random.randint(0, 1)
        inp.append(x)

   #probability value
    epsi = 0.1

# to calculate Q-value

    for i in range(10):
        #selecting a channel out of 22 channels randomly

        state = random.randint(1, 22)

        #because index starts from 0

        x = random.randint(0, 1)
        state = state - 1
        # taking action by comparing probability

        if random.uniform(0, 1) < epsi:
            ac = random.randint(0, 1)
        else:
            # taking maximum from Q - table
            ac = np.argmax(qtable[state])

      #taking reward, collision number and next state  from environment file

        nextstate, rr,c = en.take(inp[state], ac,state)

       #calculating q - value using old value

        oldval = qtable[state, ac]

       # it is the new qvalue using the given parameters

        newval = (1 - alpha) * oldval + alpha * (rr + gamma * nextstate)

       #putting the new value into the q - table

        qtable[state, ac] = newval

        # to calculate cumulative discounted reward

        R = R + pow(gamma,i) * rr *(i+1)

        #calculating cumulative collision

        C = C + c


# normalizing values
    R = R/10
    C = C/10

    RR.append(R+2)

    CC.append(C+1)
    return inp

# time steps taken 1000

for i in range(1000):

    # calling function present above

    x = DQN()




# to plot average reward graph

pl.rgraph(RR)

# to plot collision rate graph

pl.cgraph(CC)

