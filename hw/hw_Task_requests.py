import requests
from openpyxl import Workbook
server_response = requests.get("https://jsonplaceholder.typicode.com/posts")
data = server_response.json()
new_excel_file = Workbook()
new_excel_file.title = "posts.xlsx"
page = new_excel_file.active
page["A1"] = "title"
page["B1"] = "body"
a = 2
b = 2
for element in data:
    if a and b > 11:
        break
    page[f"A{a}"] = element["title"]
    page[f"B{b}"] = element["body"]
    a+=1
    b+=1

new_excel_file.save("posts.xlsx") 
