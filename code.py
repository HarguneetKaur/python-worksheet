import numpy as np
data = np.genfromtxt("sensor_data.csv", delimiter=",", skip_header=1, usecols=(1,2,3,4))
print(data)
print(type(data))
print(np.ndim(data))
print(np.shape(data))

# individual data
temp = data[:,0]
print("temp:", temp)
distance = data[:,1]
print("distance:", distance)
battery = data[:,2]
print("battery:", battery)
humidity = data[:,3]
print("humidity:", humidity)

# average of data
print(np.mean(temp))
print(np.mean(distance))
print(np.mean(battery))
print(np.mean(humidity))

# min of each data
print("minimum data")
print(np.min(temp))
print(np.min(distance))
print(np.min(battery))
print(np.min(humidity))

# max of each data
print("maximum data")
print(np.max(temp))
print(np.max(distance))
print(np.max(battery))
print(np.max(humidity))

# time when temp was highest
data2 = np.genfromtxt("sensor_data.csv", delimiter=",", skip_header=1, usecols=(0), dtype=str)
time = np.argmax(temp)
print("time:", data2[time])

with open("result1.csv", "w") as d:
    d.write("1.. mean value\n")
    d.write(f"temp:{np.mean(temp)}\n")
    d.write(f"distance:{np.mean(distance)}\n")
    d.write(f"battery:{np.mean(battery)}\n")
    d.write(f"humidity:{np.mean(humidity)}\n")

    d.write("2.. min data\n")
    d.write(f"temp:{np.min(temp)}\n")
    d.write(f"distance:{np.min(distance)}\n")
    d.write(f"battery:{np.min(battery)}\n")
    d.write(f"humidity:{np.min(humidity)}\n")

    d.write("3.. max data\n")
    d.write(f"temp:{np.max(temp)}\n")
    d.write(f"distance:{np.max(distance)}\n")
    d.write(f"battery:{np.max(battery)}\n")
    d.write(f"humidity:{np.max(humidity)}\n")

    d.write("4.. time stamp\n")
    d.write(f"time stamp:{data2[time]}\n")

y = np.sort(battery)
print(battery < 30)
yo = np.sum(battery < 30)
print(yo)

# === Project 2 ===
path = np.genfromtxt("robot_path.csv", delimiter=",", skip_header=1)

diff = np.diff(path, axis=0)
step_dist = np.linalg.norm(diff, axis=1)
total_dist = np.sum(step_dist)

dist_origin = np.linalg.norm(path, axis=1)
farthest = path[np.argmax(dist_origin)]

unique = np.unique(path, axis=0)
revisit = len(unique) != len(path)

with open("Result_2.csv", "w") as d:
    d.write(f"Total Distance: {total_dist}\n")
    d.write(f"Farthest Point: {farthest}\n")
    d.write(f"Revisited: {revisit}\n")