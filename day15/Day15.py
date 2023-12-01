sensors = open("input15.txt", "r").read().split("\n")
sensor_list, beacon_list, no_beacon, find = [], [], set(), 2000000

def get_coordinates(report):
    x = int(report.split("x=")[1].split(",")[0])
    y = int(report.split("y=")[1])
    return x, y

def get_x((x, y)):
    return x

def get_y((x, y)):
    return y

def get_distance((x1, y1), (x2, y2)):
    return abs(x1 - x2) + abs(y1 - y2)

for sensor_info in sensors:
    [sensor, beacon] = sensor_info.split(": ")
    sensor_list.append(get_coordinates(sensor))
    beacon_list.append(get_coordinates(beacon))

for s in range(len(sensor_list)):
    sensor = sensor_list[s]
    x, y = sensor
    beacon = beacon_list[s]
    diff = get_distance(sensor, beacon)

    for y2 in range(diff + 1):
        if y - y2 == find or y + y2 == find:
            for x2 in range(diff - y2 + 1):
                if y - y2 == find and beacon != (x - x2, y - y2):
                    no_beacon.add(x - x2)
                if y - y2 == find and beacon != (x + x2, y - y2):
                    no_beacon.add(x + x2)
                if y + y2 == find and beacon != (x - x2, y + y2):
                    no_beacon.add(x - x2)
                if y + y2 == find and beacon != (x + x2, y + y2):
                    no_beacon.add(x + x2)

print("first puzzle answer = " + str(len(no_beacon)))
print("second puzzle answer = " + str(0))
