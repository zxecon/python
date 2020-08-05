# Roll a dice 100 times:
# 1,2 : step - 1
# 3,4,5 : step + 1
# 6 : roll the dice again -> get the step
# step could not be negative
# Now, calculate the possiility of final steps >= 60
# %%
import numpy as np
import matplotlib.pyplot as plt

# %%
all_walks = []
np.random.seed(123)
for i in range(500) :
    random_walk = [0]
    for x in range(100) :
        step = random_walk[-1]
        dice = np.random.randint(1,7)

        if dice <= 2:
            step = max(0, step - 1)
        elif dice <= 5:
            step = step + 1
        else:
            step = step + np.random.randint(1,7)

        if np.random.rand() <= 0.001 :
            step = 0

        random_walk.append(step)
    all_walks.append(random_walk)

# %%
np_all = np.transpose(np.array(all_walks))
plt.plot(np_all)
plt.show()

# %%
ends = np_all[-1,:] # last step
plt.hist(ends)
np.mean(ends > 60)
