class String:
    def get_string(self, words):
        self.words = words

    def print_string(self):
        up = self.words.upper()
        print(up)

string = String()
string.get_string("hallo yo")
string.print_string()