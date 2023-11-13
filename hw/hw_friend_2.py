# class Contacts():
#     all_contacts=[]
#     def __init__(self, name, last_name, phone_number):
#         info = f"{last_name} {name} : {phone_number}"
#         self.all_contacts.append(info)

# class Friend(Contacts):
#     def play_football_with_me(self):
#         pass

# class ContactList(Contacts):
#     def search_by_name(self, name):
#         contacts_name = []
#         for i in self.all_contacts:
#             if name in i:
#                 contacts_name.append(i)
#             else:continue
#         return contacts_name

# con_1 = Contacts("Ularbek", "Kylychbek", 996707202228)
# con_1 = Contacts("Ularbek", "Kylychbek", 996707202221)
# con_3 = Contacts("Arnold", "Shwartneger", 996505243543)
# con_4 = Contacts("Arnold", "Kepka", 911)
# con_5 = Contacts("Marry", "Blood", 666)
# con_2 = ContactList("Tomas", "Shelby", 777)
# con_6 = ContactList("Penni", "Waiz", 2374862332)
# print(con_1.all_contacts)
# print(con_2.search_by_name("Ularbek"))
# print(con_6.search_by_name("Arnold"))
# print(con_6.search_by_name("Marry"))
# print(con_6.search_by_name("Tomas"))
# print(con_6.search_by_name("Penni"))

class Contacts():
    all_contacts = []

    def __init__(self, name, last_name, phone_number):
        self.name = name
        self.last_name = last_name
        self.phone_number = phone_number
        info = f"{last_name} {name} : {phone_number}"
        Contacts.all_contacts.append(info)

class Friend(Contacts):
    def play_football_with_me(self):
        print(f"{self.name} is playing football with me.")

class ContactList(list):
    def search_by_name(self, name):
        contacts_name = []
        for i in self:
            if name in i.name:
                contacts_name.append(i)
        return contacts_name

con_1 = Contacts("Ularbek", "Kylychbek", "996707202228")
con_3 = Contacts("Arnold", "Shwartneger", "996505243543")
con_4 = Contacts("Arnold", "Kepka", "911")
con_5 = Contacts("Marry", "Blood", "666")

contact_list = ContactList([con_1, con_3, con_4, con_5])

name_to_search = "Marry"
matching_contacts = contact_list.search_by_name(name_to_search)

if matching_contacts:
    print(f"Найдены контакты с именем '{name_to_search}':")
    for contact in matching_contacts:
        print(f"{contact.name} {contact.last_name} - {contact.phone_number}")
else:
    print(f"Контакты с именем '{name_to_search}' не найдены.")
