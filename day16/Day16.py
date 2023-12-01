valve_info = open("input16.txt", "r").read().split("\n")
valves, valve_connections, location = {}, {}, "AA"
order, score = "", 0

def best_route(from_valve):
    routes = {}
    for next_valve in valve_connections[from_valve]:
        route = [from_valve, next_valve]
        routes['-'.join(route)] = valves[next_valve]
        for next_next_valve in filter(lambda valve: valve not in [from_valve], valve_connections[next_valve]):
            routes['-'.join(route + [next_next_valve])] = valves[next_next_valve] / 2
    return max(routes, key=routes.get)

def all_routes(from_valve):
    routes = {}
    for next_valve in valve_connections[from_valve]:
        route = [from_valve, next_valve]
        routes['-'.join(route)] = valves[next_valve]
        for next_next_valve in filter(lambda valve: valve not in [from_valve], valve_connections[next_valve]):
            routes['-'.join(route + [next_next_valve])] = valves[next_next_valve] / 2
    return routes


for info in valve_info:
    [valve, others] = info.split("; ")
    valve_name = valve.split(" ")[1]
    valves[valve_name] = int(valve.split("=")[1])
    if others.find("valves") >= 0:
        valve_connections[valve_name] = others.split("valves ")[1].split(", ")
    else:
        valve_connections[valve_name] = [others.split("valve ")[1]]
for i in range(3):
    order += best_route(location)
    route = best_route(location).split("-")
    location = route[len(route) - 1]
    score += valves[location]
    print str(all_routes(location)) + ", " + location + ", " + str(valves[location])
    valves[location] = 0

print order




print("first puzzle answer = " + str(0))
print("second puzzle answer = " + str(0))
