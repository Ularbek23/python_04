my_file = open("names.txt", mode="r", encoding="utf-8")

txt = my_file.read()
print(txt)
# row = my_file.readline()
# print(row)
name_list = txt.split()
print(name_list)
my_file.close