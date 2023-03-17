import json 
import numpy as np
with open('/Users/haiyang/Desktop/selfsup_figures/debug_loss.json', 'r') as f:
    data = json.load(f)

iters, loss = [], []
for d in data:
    iters.append(d[1]/1000)
    loss.append(d[2]-1)

iters = np.array(iters).reshape(-1)
print(iters)
loss = np.array(loss).reshape(-1)

np.savetxt('/Users/haiyang/Desktop/selfsup_figures/debug_loss.dat', np.stack([iters, loss], axis=-1), fmt=['%.2f','%.5f'])