sea = []
for i in range(5):
    sea.append([])
    for j in range(5):
        sea[-1].append(' ')
ships = 3
for k in range(ships):
    y = int(input(f"координата 'y' корабля {k+1}: "))
    x = int(input(f"координата 'x' корабля {k+1}: "))
    sea[y][x] = "s"
while ships:
    for row in sea:
        for cell in row:
            print(cell, end='')
        print()
    fire_point = input("Противник стреляет: ")
    points_list = fire_point.split()
    fire_y = int(points_list[0])
    fire_x = int(points_list[1])
    if sea[fire_y][fire_x] == "s":
        sea[fire_y][fire_x] = " "
        ships -= 1
        print("Попал")
    else:
        print("Мимо")
print("End game")