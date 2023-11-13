catalog = [{
    "название": "Война и мир",
    "автор": "Лев Толстой",
    "год": 1869
}, {
    "название": "Метро 2035",
    "автор": "Дмитрий Глуховский",
    "год": 2015
}, {
    "название": "Крадущийся в тени",
    "автор": "Алексей Пехов",
    "год": 2002
}, {
    "название": "Родная кровь",
    "автор": "Anne Dar",
    "год": 2021
}, {
    "название": "Контуженный: Каторжанин",
    "автор": "Алекс Гор",
    "год": 2023
}
]
while True:
    print("Меню: ")
    print("Выберие действие:")
    print("1: Показать список книг")
    print("2: Добавить книгу")
    print("3: Выйти")
    words = input("")
    if words == "3":
        break
    if words == "1":
        for book in catalog:
            print(f"Название: {book['название']}")
            print(f"Автор: {book['автор']}" )
            print(f"Год: {book['год']}")
        
    if words == "2":
        name = input("Введите название книги: ")
        avtor = input("Введите автора книги: ")
        god = input("Введите год выпуска книги: ")
        catalog.append({
            "название": name,
            "автор": avtor,
            "год": god
        }),
        