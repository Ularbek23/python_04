while True:
    text = input("")
    if text == "exit":
        break
    elif text == '':
        print("Как классно, когда ты молчишь. Продолжай в том же духе!")
    elif not text.islower() and text.isupper():
        print("Успокойся")
    elif text[-1] == "?":
        print("Конечно")
    else:
        print("Ну и что")