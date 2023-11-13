even_numbers = []
odd_numbers = []
even_cubes = []
for i in range(1, 51):
    schet = i % 2
    if schet == 0:
        even_numbers.append(i)
    if schet != 0:
        odd_numbers.append(i)
for b in range(1, 51):
        cube = b ** 3
        ostatok_cuba = cube % 2
        if ostatok_cuba == 0:
            even_cubes.append(cube)        
             

print(even_cubes)
print(even_numbers)
print(odd_numbers)    

# even_numbers = []
# odd_numbers = []
# even_cubes = []
# for i in range(1, 51):
#     if i % 2 == 0:
#         even_numbers.append(i)
#         even_cubes.append(i ** 3)  
#     else:
#         odd_numbers.append(i)

 
# print("Четные в кубе: ", even_cubes)
# print("Четные: ", even_numbers)
# print("Нечетные: ", odd_numbers)
