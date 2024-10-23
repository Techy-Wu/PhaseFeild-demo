# This is a programme to simulate heat conduction process in simplified 1-D model
# By the use of Phase Feild Method
# Based on heat conduction equation
# $$
# \rho C_p \frac{\mathrm{d} T}{\mathrm{d} t} = \frac{\mathrm{d}}{\mathrm{d} x} (\alpha \frac{\mathrm{d} T}{\mathrm{d} x})
# $$

import matplotlib.pyplot as plt

map = []

rho = 1
alpha = 0.01
capacity = 0.05
loop_boundary = True
boundaries = [0, 100]
x_limit = 500
heat_zone = [100, 300]
total_time = 10000
time_step = 1
x_step = 1              # Distance of each cell
frame_time = 0.01       # Stop time for each frame of plot
plot_interval = 1000    # Plot every x steps

map_limit = x_limit * int(1 / x_step)

def plot(step, frame_time):
    global map, x_limit, x_step
    plt.cla()
    plt.plot(range(len(map)), map)
    plt.title('Temperature Configuration @ step = %d' % step)
    plt.xlim(1, x_limit * x_step)
    plt.ylim(0, 100)
    plt.xlabel('Index')
    plt.ylabel('Temperature')
    plt.pause(frame_time)
    plt.savefig('Step %d.png' % step)

plt.ion()

for i in range(0, map_limit + 2):
    # index 0 and map_limit + 2 are preserved as boundaries
    if i == 0:
        map.append(boundaries[0])
    elif i == map_limit + 1:
        map.append(boundaries[1])
    elif i >= heat_zone[0] and i <= heat_zone[1]:
        map.append(100)
    else:
        map.append(0)
    
    
for step in range(0, total_time * time_step + 1):
    # Update boundaries
    if loop_boundary == True:
        map[0] = map[map_limit]
        map[map_limit + 1] = map[1]
    # Update cells
    delta_Temp = []
    for index in range(1, map_limit + 1):
        dT = ((map[index - 1] + map[index + 1] - 2 * map[index]) / x_step / x_step) * alpha / capacity / rho
        delta_Temp.append(dT)
    for index in range(0, len(delta_Temp)):
        map[index + 1] += delta_Temp[index]
    # Check data range
    for index in range(1, map_limit + 1):
        if map[index] < 0:
            map[index] = 0
        elif map[index] > 100:
            map[index] = 100
    if step % plot_interval == 0:
        plot(step, frame_time)

plot(step, 0)