import matplotlib.pyplot as plt
'''
Below you will find the average accuracy for each iteration of the base case for both datasets. 
'''

# Base case CIFAR-10, DP=FALSE
N3_S100_CIFAR = [0, 0.234,	0.2805,	0.2766,	0.262,	0.2555,	0.2643,	0.2543,	0.24549999999999997,	0.2437,	0.2507]
N3_S200_CIFAR = [0, 0.267,	0.2732,	0.2854,	0.2607,	0.2793,	0.2487,	0.2892,	0.288,	0.2673,	0.2428]
N8_S100_CIFAR = [0, 0.28,	0.3019,	0.3019,	0.2784,	0.2797,	0.3064,	0.2594,	0.2921,	0.30129999999999996,	0.2883]
N8_S200_CIFAR = [0, 0.30949999999999994,	0.3219,	0.3105,	0.3281,	0.326,	0.2785,	0.328,	0.3127,	0.3106,	0.3108]


# Base case MNIST, DP=FALSE
N3_S100_MNIST = [0, 0.7463000000000001,	0.7536,	0.7889,	0.7929,	0.7864999999999999,	0.7717,	0.7912,	0.7893,	0.7696,
                 0.7707]
N3_S200_MNIST = [0, 0.8207999999999999,	0.8291,	0.832,	0.838,	0.8183000000000001,	0.8214,	0.8254,	0.8348,	0.8114,
                 0.8363999999999999]
N8_S100_MNIST = [0, 0.8285999999999999,	0.8062000000000002,	0.83,	0.8209999999999998,	0.8334,	0.8329000000000002,
                 0.8396,	0.8224999999999999,	0.8318000000000001,	0.8314000000000001]
N8_S200_MNIST = [0, 0.8417000000000001,	0.8659999999999999,	0.8646000000000001,	0.8636,	0.8632,	0.8590999999999999,
                 0.8594999999999999,	0.8608000000000001,	0.8469999999999998,	0.8678999999999999]

'''
The following two plots will provide the graphs of the base case for both datasets. 
'''
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(25, 15))
fig.suptitle("Base Case", size=30)
ax1.plot(N3_S100_MNIST, label="C = 3, S = 100")
ax1.plot(N3_S200_MNIST, label="C = 3, S = 200")
ax1.plot(N8_S100_MNIST, label="C = 8, S = 100")
ax1.plot(N8_S200_MNIST, label="C = 8, S = 200")
ax1.set_title("MNIST", size=20)
ax1.set_xlabel("Number of Iterations (N)", size=20)
ax1.set_ylabel("Accuracy (%)", size=20)
ax1.legend(loc="upper right", fontsize=20)
ax1.set_xlim(1, 10)
ax1.set_ylim(0.73, 0.9)

ax2.plot(N3_S100_CIFAR, label="C = 3, S = 100")
ax2.plot(N3_S200_CIFAR, label="C = 3, S = 200")
ax2.plot(N8_S100_CIFAR, label="C = 8, S = 100")
ax2.plot(N8_S200_CIFAR, label="C = 8, S = 200")
ax2.set_title("CIFAR-10", size=20)
ax2.set_xlabel("Number of Iterations (N)", size=20)
ax2.set_ylabel("Accuracy (%)", size=20)
ax2.legend(loc="upper right", fontsize=20)
ax2.set_xlim(1, 10)
ax2.set_ylim(0.22, 0.35)

plt.show()
