import matplotlib.pyplot as plt

# to plot reward graph

def rgraph(RR):
    # plotting the points

    for i in range(1000):

        # put a condition to get a less denser graph . Then, it will become easier to compare.

        if RR[i] > 2.0:
            plt.plot(i,RR[i],'rs',color = 'red')

    # naming the x axis

    plt.xlabel('time steps')
    plt.xlim(0,1000)

    # naming the y axis

    plt.ylabel('average reward')
    plt.ylim(0,6)


    plt.show()

# to plot collision rate graph
def cgraph(CC):

    # plotting the points

    for i in range(1000):

        # put a condition to get a less denser graph . Then, it will become easier to compare.

         if CC[i] > 1:
             plt.plot(i,CC[i],'bs',color = 'black')

    # naming the x axis

    plt.xlabel('time steps')
    plt.xlim(0,1000)

    # naming the y axis

    plt.ylabel('collision rate')
    plt.ylim(0,10)



    plt.show()