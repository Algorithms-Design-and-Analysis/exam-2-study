def full_tank(fuel_capacity, starting_city, final_city, roads, prices):
    return True

def main():
    _, roads_number = input().split(' ')
    prices = input().split(' ')
    for pos in range(len(prices)):
        prices[pos] = int(prices[pos])
    roads = []
    for _ in range(int(roads_number)):
        roads.append(input().split(' '))
    for i in range(len(roads)):
        for j in range(len(roads[0])):
            roads[i][j] = int(roads[i][j])
    queries_number = input()
    for _ in range(int(queries_number)):
        fuel_capacity, starting_city, final_city = input().split(' ')
        print(full_tank(int(fuel_capacity), int(starting_city), int(final_city), roads, prices))
