spis = []
my_post = {
    "post": {
        "name": "Python",
        "comments": [
            {
                "id": "1",
                "text": "ok, that's good",
            },
            {
                "id": "6",
                "text": "not bad",
            },
        ]
    },
    "userId": 1,
    "id": 1,
}
print(my_post["post"]["comments"][0]["text"], my_post["post"]["comments"][1]["text"])
n = my_post["post"]["comments"][0]["text"], my_post["post"]["comments"][1]["text"]
for comment in my_post["post"]["comments"]:
    spis.append(comment["text"])
print(spis)