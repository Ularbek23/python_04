import requests
url = "https://api.telegram.org/bot6450383163:AAHb6Do-tMkORRBWdQjAyZrXyWyq1-1teC0/"
# response = requests.get(f"{url}getUpdates")
# data = response.json()
# print(data)
chat_id = 1020812876
text = "@-->-"
requests.get(f"{url}SendMessage?chat_id={chat_id}&text={text}")